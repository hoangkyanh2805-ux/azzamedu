/* global SHOP_CONFIG */

const FALLBACK_CATEGORIES = [
  { id: "khoa_hoc", label: "📚 Khóa học", sort_order: 1 },
  { id: "membership", label: "🏛 Membership", sort_order: 2 },
  { id: "free", label: "🎁 Free", sort_order: 3 },
  { id: "services", label: "🔧 Services", sort_order: 4 },
];

const FALLBACK_OFFERS = [
  {
    sku: "AE-APP-001",
    name: "Apprentice Operating Course",
    display_name: "Apprentice Operating Course",
    category: "khoa_hoc",
    emoji: "📘",
    kind: "checkout",
    price_usd: 297,
    checkout_path: "/checkout/?add-to-cart=AE-APP-001",
    sort_order: 1,
  },
  {
    sku: "AE-VIP-MON",
    name: "VIP Private Desk — Monthly",
    display_name: "VIP Private Desk — Monthly",
    category: "membership",
    emoji: "🏛",
    kind: "checkout",
    price_usd: 149,
    checkout_path: "/checkout/?add-to-cart=AE-VIP-MON",
    sort_order: 2,
  },
  {
    sku: "AE-VIP-YR",
    name: "VIP Private Desk — Annual",
    display_name: "VIP Private Desk — Annual",
    category: "membership",
    emoji: "🏛",
    kind: "checkout",
    price_usd: 1290,
    checkout_path: "/checkout/?add-to-cart=AE-VIP-YR",
    sort_order: 3,
  },
  {
    sku: "AE-QNT-001",
    name: "Quant Desk",
    display_name: "Quant Desk",
    category: "membership",
    emoji: "📊",
    kind: "apply",
    apply_path: "/quant-desk",
    price_usd: null,
    checkout_path: "/quant-desk",
    sort_order: 4,
  },
  {
    sku: "AE-GP-000",
    name: "2% Rule Gameplan",
    display_name: "2% Rule Gameplan",
    category: "free",
    emoji: "🎁",
    kind: "gameplan",
    price_usd: null,
    checkout_path: "/gameplan",
    sort_order: 1,
  },
  {
    sku: "AE-DWY-001",
    name: "DWY Bot & Broker Setup",
    display_name: "DWY Bot & Broker Setup",
    category: "services",
    emoji: "🔧",
    kind: "callback",
    price_usd: 497,
    checkout_path: "/checkout/?add-to-cart=AE-DWY-001",
    sort_order: 5,
  },
];

function shopConfig() {
  return window.SHOP_CONFIG || {};
}

function supabaseHeaders(anonKey) {
  return {
    apikey: anonKey,
    Authorization: `Bearer ${anonKey}`,
    Accept: "application/json",
  };
}

async function supabaseGet(baseUrl, anonKey, path) {
  const res = await fetch(`${baseUrl.replace(/\/$/, "")}/rest/v1/${path}`, {
    headers: supabaseHeaders(anonKey),
  });
  if (!res.ok) {
    throw new Error(`Supabase ${res.status}: ${path}`);
  }
  return res.json();
}

async function loadShopCatalog() {
  const cfg = shopConfig();
  const { supabaseUrl, supabaseAnonKey } = cfg;
  if (!supabaseUrl || !supabaseAnonKey) {
    return {
      categories: FALLBACK_CATEGORIES,
      offers: FALLBACK_OFFERS,
      source: "fallback",
    };
  }

  const [categories, offers] = await Promise.all([
    supabaseGet(
      supabaseUrl,
      supabaseAnonKey,
      "shop_categories?select=id,label,sort_order&active=eq.true&order=sort_order.asc"
    ),
    supabaseGet(
      supabaseUrl,
      supabaseAnonKey,
      "offers?select=*&active=eq.true&active_on_bot=eq.true&order=sort_order.asc,category.asc,sku.asc"
    ),
  ]);

  return { categories, offers, source: "supabase" };
}

function offerDisplayName(offer) {
  return offer.display_name || offer.name || offer.sku;
}

function absoluteUrl(path) {
  const cfg = shopConfig();
  const base = (cfg.siteBaseUrl || "").replace(/\/$/, "");
  if (!path) return base;
  if (path.startsWith("http")) return path;
  return `${base}${path.startsWith("/") ? "" : "/"}${path}`;
}

function gameplanUrl() {
  const cfg = shopConfig();
  return absoluteUrl(cfg.gameplanPath || "/gameplan");
}

function offerActionUrl(offer) {
  const kind = offer.kind || "checkout";
  if (kind === "gameplan") return gameplanUrl();
  if (kind === "apply") return absoluteUrl(offer.apply_path || offer.checkout_path);
  return absoluteUrl(offer.checkout_path);
}

function priceLabel(offer) {
  const kind = offer.kind || "checkout";
  if (kind === "gameplan") return "Free";
  if (kind === "apply") return "Apply";
  if (kind === "callback") return "Request";
  const price = offer.price_usd;
  if (price == null || price === "") return "";
  const n = Number(price);
  if (offer.sku.endsWith("-MON")) return `$${n}/mo`;
  if (offer.sku.endsWith("-YR")) return `$${n}/yr`;
  return `$${n}`;
}

function mainButtonLabel(offer) {
  const kind = offer.kind || "checkout";
  const price = priceLabel(offer);
  if (kind === "gameplan") return "Get Free Gameplan";
  if (kind === "apply") return "Apply";
  if (kind === "callback") return "Contact via bot";
  return price ? `Pay ${price}` : "Continue";
}

function offersInCategory(offers, categoryId) {
  return offers.filter((o) => (o.category || "general") === categoryId);
}
