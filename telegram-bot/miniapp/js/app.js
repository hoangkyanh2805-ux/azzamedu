/* global Telegram, loadShopCatalog, offerDisplayName, offersInCategory,
   priceLabel, mainButtonLabel, offerActionUrl, shopConfig */

const state = {
  view: "categories",
  categoryId: null,
  offer: null,
  catalog: null,
};

const $ = (sel) => document.querySelector(sel);

function tg() {
  return window.Telegram && window.Telegram.WebApp;
}

function initTelegram() {
  const webapp = tg();
  if (!webapp) return;
  webapp.ready();
  webapp.expand();
  webapp.setHeaderColor("secondary_bg_color");
}

function hideBottomButtons() {
  const webapp = tg();
  if (!webapp) return;
  webapp.MainButton.hide();
  webapp.SecondaryButton.hide();
  if (webapp.BackButton) webapp.BackButton.hide();
}

function setHeader(title, subtitle) {
  $("#header-title").textContent = title;
  $("#header-sub").textContent = subtitle || "";
}

function showLoading(show) {
  $("#loading").hidden = !show;
  $("#view").hidden = show;
}

function showError(message) {
  const el = $("#error");
  el.hidden = false;
  el.textContent = message;
}

function clearError() {
  const el = $("#error");
  el.hidden = true;
  el.textContent = "";
}

function renderCategories() {
  state.view = "categories";
  state.categoryId = null;
  state.offer = null;
  hideBottomButtons();
  setHeader("Alpha Elite Shop", state.catalog.source === "supabase" ? "Live catalog" : "Demo catalog");

  const root = $("#view");
  root.innerHTML = "";
  const list = document.createElement("div");
  list.className = "card-list";

  for (const cat of state.catalog.categories) {
    const count = offersInCategory(state.catalog.offers, cat.id).length;
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "card";
    btn.innerHTML = `<span class="card-title">${cat.label}</span><span class="card-meta">${count} offer${count === 1 ? "" : "s"}</span>`;
    btn.addEventListener("click", () => renderOffers(cat.id));
    list.appendChild(btn);
  }
  root.appendChild(list);
}

function renderOffers(categoryId) {
  state.view = "offers";
  state.categoryId = categoryId;
  state.offer = null;
  hideBottomButtons();

  const cat = state.catalog.categories.find((c) => c.id === categoryId);
  setHeader(cat ? cat.label : "Products", "Chọn sản phẩm");

  const webapp = tg();
  if (webapp && webapp.BackButton) {
    webapp.BackButton.offClick();
    webapp.BackButton.show();
    webapp.BackButton.onClick(renderCategories);
  }

  const items = offersInCategory(state.catalog.offers, categoryId);
  const root = $("#view");
  root.innerHTML = "";
  const list = document.createElement("div");
  list.className = "card-list";

  for (const offer of items) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "card card-offer";
    const emoji = offer.emoji || "📦";
    const price = priceLabel(offer);
    btn.innerHTML = `
      <span class="card-title">${emoji} ${offerDisplayName(offer)}</span>
      <span class="card-meta">${price || offer.sku}</span>`;
    btn.addEventListener("click", () => renderDetail(offer));
    list.appendChild(btn);
  }
  root.appendChild(list);
}

function renderDetail(offer) {
  state.view = "detail";
  state.offer = offer;

  const webapp = tg();
  if (webapp && webapp.BackButton) {
    webapp.BackButton.offClick();
    webapp.BackButton.show();
    webapp.BackButton.onClick(() => renderOffers(state.categoryId));
  }

  const emoji = offer.emoji || "";
  const name = offerDisplayName(offer);
  setHeader(`${emoji} ${name}`.trim(), offer.sku);

  const root = $("#view");
  const price = priceLabel(offer);
  const kind = offer.kind || "checkout";
  const isVip = offer.sku.startsWith("AE-VIP-");

  root.innerHTML = `
    <div class="detail">
      ${price ? `<p class="detail-price">${price}</p>` : ""}
      <p class="detail-kind">${kindLabel(kind)}</p>
      ${isVip ? `
        <label class="field">
          <span class="field-label">Telegram @username (sau khi mua)</span>
          <input id="vip-username" type="text" placeholder="@yourname" autocomplete="username" />
        </label>` : ""}
      <p class="hint">Thanh toán qua FunnelKit + PayPal trên website. Education only — not investment advice.</p>
    </div>`;

  setupDetailButtons(offer, isVip);
}

function kindLabel(kind) {
  const map = {
    checkout: "Thanh toán trực tuyến",
    gameplan: "Tài liệu miễn phí",
    apply: "Đơn đăng ký",
    callback: "Liên hệ qua bot",
  };
  return map[kind] || kind;
}

function setupDetailButtons(offer, isVip) {
  const webapp = tg();
  if (!webapp) return;

  webapp.SecondaryButton.setText("« Danh mục").offClick().onClick(() => {
    renderOffers(state.categoryId);
  }).show();

  const label = mainButtonLabel(offer);
  webapp.MainButton.setText(label).offClick().onClick(() => {
    onMainAction(offer, isVip);
  }).show();
}

function onMainAction(offer, isVip) {
  const webapp = tg();
  const kind = offer.kind || "checkout";

  if (isVip) {
    const input = $("#vip-username");
    const raw = input && input.value.trim();
    if (!raw) {
      if (webapp) webapp.showAlert("Nhập @telegram username để add VIP sau khi mua.");
      return;
    }
  }

  if (kind === "callback") {
    if (webapp) {
      webapp.showAlert("Quay lại bot → Shop → DWY để đặt lịch tư vấn.");
      webapp.close();
    }
    return;
  }

  const url = offerActionUrl(offer);
  if (!url) {
    if (webapp) webapp.showAlert("Checkout URL chưa cấu hình.");
    return;
  }

  if (webapp) {
    webapp.MainButton.showProgress(false);
    if (webapp.HapticFeedback) webapp.HapticFeedback.impactOccurred("medium");
    webapp.openLink(url, { try_instant_view: false });
    webapp.MainButton.hideProgress();
  } else {
    window.open(url, "_blank");
  }
}

async function boot() {
  initTelegram();
  showLoading(true);
  clearError();

  try {
    state.catalog = await loadShopCatalog();
    showLoading(false);
    renderCategories();
  } catch (err) {
    showLoading(false);
    console.error(err);
    showError(`Không tải được catalog: ${err.message}`);
    window.SHOP_CONFIG = { ...(window.SHOP_CONFIG || {}), supabaseUrl: "", supabaseAnonKey: "" };
    state.catalog = await loadShopCatalog();
    renderCategories();
  }
}

document.addEventListener("DOMContentLoaded", boot);
