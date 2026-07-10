"""Data layer with memory + Supabase backends."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

import httpx


def _now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class Member:
    telegram_id: int
    telegram_username: Optional[str] = None
    email: Optional[str] = None
    tier: str = "free"
    status: str = "lead"
    sku_last: Optional[str] = None
    vip_username: Optional[str] = None


@dataclass
class QueueItem:
    queue_code: str
    telegram_id: int
    request_type: str
    sku: Optional[str] = None
    email: Optional[str] = None
    status: str = "payment_review"
    payment_proof_ref: Optional[str] = None
    created_at: datetime = field(default_factory=_now)


@dataclass
class Ticket:
    ticket_code: str
    telegram_id: int
    message: str
    status: str = "open"
    created_at: datetime = field(default_factory=_now)


class MemoryStore:
    def __init__(self) -> None:
        self.members: dict[int, Member] = {}
        self.queue: dict[str, QueueItem] = {}
        self.tickets: dict[str, Ticket] = {}
        self._queue_seq = 0
        self._ticket_seq = 0

    def upsert_member(self, telegram_id: int, username: Optional[str] = None) -> Member:
        if telegram_id not in self.members:
            self.members[telegram_id] = Member(telegram_id=telegram_id)
        m = self.members[telegram_id]
        if username:
            m.telegram_username = username
        return m

    def link_email(self, telegram_id: int, email: str) -> Member:
        m = self.upsert_member(telegram_id)
        m.email = email.strip().lower()
        return m

    def next_queue_code(self) -> str:
        self._queue_seq += 1
        return f"AE-{datetime.now().year}-{self._queue_seq:04d}"

    def next_ticket_code(self) -> str:
        self._ticket_seq += 1
        return f"SUP-{self._ticket_seq:04d}"

    def add_queue(
        self,
        telegram_id: int,
        request_type: str,
        sku: Optional[str] = None,
        email: Optional[str] = None,
        proof: Optional[str] = None,
    ) -> QueueItem:
        code = self.next_queue_code()
        item = QueueItem(
            queue_code=code,
            telegram_id=telegram_id,
            request_type=request_type,
            sku=sku,
            email=email,
            payment_proof_ref=proof,
        )
        self.queue[code] = item
        m = self.upsert_member(telegram_id)
        m.status = "payment_review"
        if sku:
            m.sku_last = sku
        return item

    def add_ticket(self, telegram_id: int, message: str) -> Ticket:
        code = self.next_ticket_code()
        t = Ticket(ticket_code=code, telegram_id=telegram_id, message=message)
        self.tickets[code] = t
        return t

    def pending_queue(self) -> list[QueueItem]:
        open_status = {
            "payment_review",
            "payment_confirmed",
            "provisioning",
            "tg_pending",
        }
        return [q for q in self.queue.values() if q.status in open_status]

    def get_queue(self, code: str) -> Optional[QueueItem]:
        return self.queue.get(code.upper())

    def set_queue_status(self, code: str, status: str) -> Optional[QueueItem]:
        item = self.queue.get(code.upper())
        if not item:
            return None
        item.status = status
        m = self.members.get(item.telegram_id)
        if m:
            m.status = status
            if status == "access_active_vip":
                m.tier = "vip"
            elif status == "lh_active_apprentice":
                m.tier = "apprentice"
        return item

    def get_member(self, telegram_id: int) -> Optional[Member]:
        return self.members.get(telegram_id)

    def list_shop_categories(self) -> list[dict]:
        from bot.catalog import DEFAULT_CATEGORIES

        return [{"id": c.id, "label": c.label, "sort_order": i} for i, c in enumerate(DEFAULT_CATEGORIES)]

    def list_shop_offers(self, active_only: bool = True) -> list[dict]:
        from bot.catalog import DEFAULT_OFFERS

        rows = []
        for o in DEFAULT_OFFERS:
            rows.append(
                {
                    "sku": o.sku,
                    "name": o.name,
                    "display_name": None,
                    "category": o.category_id,
                    "emoji": o.emoji,
                    "kind": o.kind,
                    "callback_data": o.callback_data or None,
                    "apply_path": o.apply_path or None,
                    "checkout_path": None,
                    "price_usd": None,
                    "sort_order": 0,
                    "active": True,
                    "active_on_bot": True,
                }
            )
        return rows

    def upsert_shop_category(self, payload: dict) -> None:
        pass

    def upsert_offer(self, payload: dict) -> None:
        pass


class SupabaseStore:
    """Minimal PostgREST adapter for production persistence."""

    def __init__(self, supabase_url: str, service_key: str) -> None:
        self.base = f"{supabase_url.rstrip('/')}/rest/v1"
        self.headers = {
            "apikey": service_key,
            "Authorization": f"Bearer {service_key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
        }

    def _request(self, method: str, path: str, extra_headers: dict | None = None, **kwargs) -> httpx.Response:
        headers = {**self.headers, **(extra_headers or {})}
        response = httpx.request(
            method=method,
            url=f"{self.base}{path}",
            headers=headers,
            timeout=15,
            **kwargs,
        )
        response.raise_for_status()
        return response

    def _next_queue_code(self) -> str:
        year = datetime.now().year
        rows = self._request("GET", "/provision_queue?select=queue_code").json()
        return f"AE-{year}-{len(rows) + 1:04d}"

    def _next_ticket_code(self) -> str:
        rows = self._request("GET", "/support_tickets?select=ticket_code").json()
        return f"SUP-{len(rows) + 1:04d}"

    def upsert_member(self, telegram_id: int, username: Optional[str] = None) -> Member:
        payload = {"telegram_id": telegram_id}
        if username:
            payload["telegram_username"] = username
        self._request(
            "POST",
            "/members?on_conflict=telegram_id",
            extra_headers={"Prefer": "resolution=merge-duplicates,return=representation"},
            json=payload,
        )
        rows = self._request("GET", f"/members?telegram_id=eq.{telegram_id}&select=*").json()
        row = rows[0]
        return Member(
            telegram_id=row["telegram_id"],
            telegram_username=row.get("telegram_username"),
            email=row.get("email"),
            tier=row.get("tier", "free"),
            status=row.get("status", "lead"),
            sku_last=row.get("sku_last"),
            vip_username=row.get("vip_username"),
        )

    def link_email(self, telegram_id: int, email: str) -> Member:
        email = email.strip().lower()
        self._request("PATCH", f"/members?telegram_id=eq.{telegram_id}", json={"email": email})
        return self.upsert_member(telegram_id)

    def add_queue(
        self,
        telegram_id: int,
        request_type: str,
        sku: Optional[str] = None,
        email: Optional[str] = None,
        proof: Optional[str] = None,
    ) -> QueueItem:
        code = self._next_queue_code()
        payload = {
            "queue_code": code,
            "telegram_id": telegram_id,
            "request_type": request_type,
            "sku": sku,
            "email": email,
            "payment_proof_ref": proof,
            "status": "payment_review",
        }
        self._request("POST", "/provision_queue", json=payload)
        self._request(
            "PATCH",
            f"/members?telegram_id=eq.{telegram_id}",
            json={"status": "payment_review", "sku_last": sku},
        )
        return QueueItem(
            queue_code=code,
            telegram_id=telegram_id,
            request_type=request_type,
            sku=sku,
            email=email,
            payment_proof_ref=proof,
            status="payment_review",
        )

    def add_ticket(self, telegram_id: int, message: str) -> Ticket:
        code = self._next_ticket_code()
        self._request(
            "POST",
            "/support_tickets",
            json={
                "ticket_code": code,
                "telegram_id": telegram_id,
                "message": message,
                "status": "open",
            },
        )
        return Ticket(ticket_code=code, telegram_id=telegram_id, message=message)

    def pending_queue(self) -> list[QueueItem]:
        statuses = "payment_review,payment_confirmed,provisioning,tg_pending"
        rows = self._request(
            "GET",
            f"/provision_queue?select=queue_code,telegram_id,request_type,sku,email,status,payment_proof_ref,created_at&status=in.({statuses})&order=created_at.desc",
        ).json()
        return [
            QueueItem(
                queue_code=r["queue_code"],
                telegram_id=r["telegram_id"],
                request_type=r["request_type"],
                sku=r.get("sku"),
                email=r.get("email"),
                status=r.get("status", "payment_review"),
                payment_proof_ref=r.get("payment_proof_ref"),
            )
            for r in rows
        ]

    def get_queue(self, code: str) -> Optional[QueueItem]:
        rows = self._request(
            "GET",
            f"/provision_queue?queue_code=eq.{code.upper()}&select=queue_code,telegram_id,request_type,sku,email,status,payment_proof_ref,created_at",
        ).json()
        if not rows:
            return None
        r = rows[0]
        return QueueItem(
            queue_code=r["queue_code"],
            telegram_id=r["telegram_id"],
            request_type=r["request_type"],
            sku=r.get("sku"),
            email=r.get("email"),
            status=r.get("status", "payment_review"),
            payment_proof_ref=r.get("payment_proof_ref"),
        )

    def set_queue_status(self, code: str, status: str) -> Optional[QueueItem]:
        item = self.get_queue(code)
        if not item:
            return None
        self._request("PATCH", f"/provision_queue?queue_code=eq.{code.upper()}", json={"status": status})
        tier = None
        if status == "access_active_vip":
            tier = "vip"
        elif status == "lh_active_apprentice":
            tier = "apprentice"
        member_payload = {"status": status}
        if tier:
            member_payload["tier"] = tier
        self._request("PATCH", f"/members?telegram_id=eq.{item.telegram_id}", json=member_payload)
        item.status = status
        return item

    def get_member(self, telegram_id: int) -> Optional[Member]:
        rows = self._request("GET", f"/members?telegram_id=eq.{telegram_id}&select=*").json()
        if not rows:
            return None
        row = rows[0]
        return Member(
            telegram_id=row["telegram_id"],
            telegram_username=row.get("telegram_username"),
            email=row.get("email"),
            tier=row.get("tier", "free"),
            status=row.get("status", "lead"),
            sku_last=row.get("sku_last"),
            vip_username=row.get("vip_username"),
        )

    def list_shop_categories(self) -> list[dict]:
        rows = self._request(
            "GET",
            "/shop_categories?select=id,label,sort_order&active=eq.true&order=sort_order.asc",
        ).json()
        return rows

    def list_shop_offers(self, active_only: bool = True) -> list[dict]:
        path = "/offers?select=*&order=sort_order.asc,category.asc,sku.asc"
        if active_only:
            path += "&active=eq.true&active_on_bot=eq.true"
        return self._request("GET", path).json()

    def upsert_shop_category(self, payload: dict) -> None:
        body = {
            "id": payload["id"],
            "label": payload["label"],
            "sort_order": payload.get("sort_order", 0),
            "active": payload.get("active", True),
        }
        self._request(
            "POST",
            "/shop_categories?on_conflict=id",
            extra_headers={"Prefer": "resolution=merge-duplicates"},
            json=body,
        )

    def upsert_offer(self, payload: dict) -> None:
        clean = {k: v for k, v in payload.items() if v is not None}
        self._request(
            "POST",
            "/offers?on_conflict=sku",
            extra_headers={"Prefer": "resolution=merge-duplicates,return=representation"},
            json=clean,
        )


class StoreProxy:
    """Keeps one stable object reference across imports."""

    def __init__(self, backend: MemoryStore | SupabaseStore) -> None:
        self.backend = backend

    def set_backend(self, backend: MemoryStore | SupabaseStore) -> None:
        self.backend = backend

    def __getattr__(self, name: str):
        return getattr(self.backend, name)


def init_store(provider: str, database_url: str, supabase_service_key: str) -> None:
    if provider == "supabase" and database_url and supabase_service_key:
        store.set_backend(SupabaseStore(supabase_url=database_url, service_key=supabase_service_key))
        return
    store.set_backend(MemoryStore())


store = StoreProxy(MemoryStore())
