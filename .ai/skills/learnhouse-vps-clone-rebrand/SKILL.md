---
name: learnhouse-vps-clone-rebrand
description: >-
  Clone a working LearnHouse VPS (panel backup/restore) onto a new VPS, then
  rebrand domain so images/logo/thumbnails work. Use when the user clones
  LearnHouse between iNET VPS boxes, reports broken images after clone, needs
  domain migrate + SSL for a new learn.* host, or prepares another brand/channel
  instance (e.g. Azzam Gold / alex-mentor / Tom Bennett / Eddric).
---

# LearnHouse — VPS Clone + Domain Rebrand

## When to use

- Panel **backup VPS1 → restore VPS2** (OS image named `*_Backup-*`)
- Site text OK but **logo / thumbnail / lesson images broken**
- F12 shows old domain in `og:image` / favicon / `/content/...`
- Spinning up another brand LMS from an existing LearnHouse (Alex Mentor, Tom Bennett, …)

## Proven instances

| Brand / channel | LMS domain | Notes |
|-----------------|------------|--------|
| Azzam Gold (source) | `https://learn.azzamedu.com` | VPS1 source of truth for clone |
| Alex Mentor | `https://learn.alex-mentor.com` | Cloned from azzamedu; fixed 2026-07-20 |
| Tom Bennett Trading Expert | `https://learn.tom-edu.com` | Cloned from alex-mentor snapshot; fixed 2026-07-23. Telegram: [t.me/TomBennettTradingExpert](https://t.me/TomBennettTradingExpert) |
| Eddric | *(pending)* | Next clone target. Need: LMS domain + VPS IP + SSH port + root password after Reset. Preferred source: `learn.tom-edu.com` or `learn.alex-mentor.com`. |

Do **not** put root passwords in this skill. Use gitignored env files under `web/learnhouse/scripts/`.

## Root cause (after panel clone)

1. **Config still has old domain** — `LEARNHOUSE_DOMAIN`, `NEXT_PUBLIC_*`, `NEXTAUTH_URL`, `LEARNHOUSE_COOKIE_DOMAIN`
2. **DB stores absolute media URLs** with old host → browser requests wrong host
3. **SSL cert** still for old domain → nginx crash-loop if conf points to missing `live/<new-domain>/`
4. Media files usually **are** in Docker volume `*_learnhouse_content_*` (check before re-uploading)

Install dir on these boxes is **`/root/.learnhouse/default`**, not `/opt/learnhouse` (that path may be empty).

## Inputs required from user

```text
OLD_DOMAIN=learn.<source>.com
NEW_DOMAIN=learn.<new>.com
NEW_TOP=<new>.com          # cookie / TOP_DOMAIN
VPS_HOST=<new VPS IP>
VPS_PORT=<SSH port, often 24700>
VPS_PASSWORD=<from panel Reset mật khẩu — clone PW ≠ source PW>
```

DNS A record for `NEW_DOMAIN` → `VPS_HOST` before SSL.

## Workflow checklist

```text
Clone rebrand progress:
- [ ] 1. SSH works (probe ports 24700/22; use new root password)
- [ ] 2. Locate install: /root/.learnhouse/default (.env, docker-compose, nginx.prod.conf)
- [ ] 3. Confirm docker: learnhouse-app / db / redis / nginx
- [ ] 4. Replace OLD_DOMAIN + OLD_TOP in .env, config, nginx, compose
- [ ] 5. docker compose up -d --force-recreate
- [ ] 6. Postgres: replace old host in text/json/jsonb columns
- [ ] 7. Issue SSL for NEW_DOMAIN (HTTP ACME → full SSL nginx)
- [ ] 8. Verify: HTML has no OLD_DOMAIN; /content/... returns 200
```

## Scripts (repo)

| Script | Role |
|--------|------|
| `web/learnhouse/scripts/fix-alex-mentor-clone.sh` | Domain + DB URL replace for install at `/root/.learnhouse/default` |
| `web/learnhouse/scripts/fix-alex-mentor-ssl.sh` | Certbot webroot + SSL nginx (pattern from `enable-https.sh`) |
| `web/learnhouse/scripts/run-alex-mentor-fix.py` | SSH upload/run clone fix |
| `web/learnhouse/scripts/run-alex-mentor-ssl.py` | SSH upload/run SSL fix |
| `web/learnhouse/scripts/run-tom-bennett-rebrand.py` | Full rebrand runner (clone fix + SSL) via `deploy-tom-bennett.env` |
| `web/learnhouse/scripts/deploy-alex-mentor.env` / `deploy-tom-bennett.env` | **Gitignored** per-brand creds |
| `web/learnhouse/scripts/enable-https.sh` | Original HTTPS helper (azzamedu) |

For a **new** brand (Eddric next):

1. Create `deploy-eddric.env` (gitignored) from the template fields in Inputs
2. Prefer source snapshot from a **already-fixed** LMS (`learn.tom-edu.com` or `learn.alex-mentor.com`)
3. Run parameterized fix: same shell scripts + `OLD_*` / `NEW_*` / `LEARNHOUSE_INSTALL_DIR=/root/.learnhouse/default`
4. Or copy `run-tom-bennett-rebrand.py` → `run-eddric-rebrand.py` pointing at `deploy-eddric.env`

## Diagnose in 2 minutes

**F12 → Elements / Network on broken image**

| Observation | Action |
|-------------|--------|
| `src` still old domain | Config + DB replace |
| `src` new domain but **404** | Content volume missing/empty — copy volume from source VPS |
| Nginx Restarting; logs `cannot load certificate ... live/<new>` | Run SSL fix / `enable-https.sh` pattern |
| Site 200, favicon 200, no old domain in HTML | Done — user hard-refresh |

Quick verify from agent machine:

```python
# homepage 200, no old domain string, content URL 200
```

## SSH notes (iNET)

- New VPS after restore: **Reset mật khẩu** — source VPS password usually fails
- SSH often on **24700**, not 22
- Never commit passwords; never paste long-lived secrets into skill docs

## SSL pattern (must follow order)

1. Write **HTTP-only** nginx with `/.well-known/acme-challenge/` → `/var/www/certbot`
2. Recreate nginx so port 80 works
3. `certbot certonly --webroot -w /var/www/certbot -d NEW_DOMAIN`
4. Write full SSL nginx (80→443 redirect + 443 ssl)
5. Recreate nginx; confirm `HTTPS 200`

Do not point nginx at `live/NEW_DOMAIN` until the cert exists (or nginx loops).

## Tom Bennett — done

- LMS: `https://learn.tom-edu.com`
- Runner: `web/learnhouse/scripts/run-tom-bennett-rebrand.py`
- Channel: [t.me/TomBennettTradingExpert](https://t.me/TomBennettTradingExpert)

## Eddric — prep (next)

When user provides LMS domain + VPS:

1. Decide source clone (prefer `learn.tom-edu.com` or `learn.alex-mentor.com`)
2. Panel backup/snapshot → new VPS
3. DNS `learn.<eddric-domain>` → new IP
4. Reset root password on new VPS
5. Send agent: `OLD_DOMAIN`, `NEW_DOMAIN`, `NEW_TOP`, `VPS_HOST`, `VPS_PORT`, `VPS_PASSWORD`
6. Agent runs this skill end-to-end
7. Rebrand org name / logo in LearnHouse UI after images work
8. Wire Eddric Telegram channel / bot separately (out of scope of media fix)

Paste template for agent:

```text
Dùng skill learnhouse-vps-clone-rebrand cho Eddric
OLD_DOMAIN=learn.tom-edu.com
NEW_DOMAIN=learn.<eddric>.com
NEW_TOP=<eddric>.com
VPS_HOST=...
VPS_PORT=24700
VPS_PASSWORD=...
```

## Do not

- Re-seed course just to fix images (wipes UI edits)
- Assume install is `/opt/learnhouse`
- Reuse source VPS password on clone without testing
- Commit `deploy-*.env`

## Related

- Day-to-day content sync (not clone): `.ai/skills/learnhouse-production-sync/SKILL.md`
- Domain migrate in-place (same VPS): `migrate-domain.py` / `migrate-domain.sh`
