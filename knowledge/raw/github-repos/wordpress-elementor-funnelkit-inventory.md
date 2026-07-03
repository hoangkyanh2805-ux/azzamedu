# GitHub / Source Inventory — WordPress · Elementor · FunnelKit

> Mapped for Alpha Elite `web/wordpress/` — verified sources + reuse pattern only (no blind copy).

---

## P0 — Dùng ngay cho project này

| Source | URL | Confidence | Reuse pattern | Alpha Elite asset |
|--------|-----|------------|---------------|-------------------|
| **Hello Elementor Child** | https://github.com/elementor/hello-theme-child | High | Child theme scaffold, `functions.php` enqueue | `import/alpha-elite-child-elementor/` |
| **Elementor core** | https://github.com/elementor/elementor | High | `wp_slash()` + `_elementor_data` meta write | `import/ae-setup-once.php` |
| **Elementor MCP** | https://github.com/msrbuilds/elementor-mcp | High | `import-template`, `create-page`, clone-and-mutate | Future: agent-driven page gen |
| **WooCommerce WC-CLI** | https://github.com/woocommerce/woocommerce (docs/wc-cli) | High | `wp wc product create --sku=...` | `import/ae-setup-products.php` |
| **WP-CLI handbook** | https://github.com/wp-cli/handbook | High | `wp eval-file` one-shot scripts | Setup scripts pattern |
| **FunnelKit docs** | https://funnelkit.com/docs/checkout-pages/elementor/ | High | Checkout widgets, dark templates import | `docs/funnelkit-elementor-setup.md` |
| **CartFlows (WP.org)** | https://wordpress.org/plugins/cartflows/ | High | Funnel step model, store checkout override | FunnelKit alt if license issue |
| **marketingskills** | https://github.com/coreyhaines31/marketingskills | High | page-cro, form-cro, pricing-strategy | `docs/repo_skill_map.md` |
| **web-quality-skills** | https://github.com/addyosmani/web-quality-skills | High | Pre-launch Lighthouse gate | `.ai/agents/web-quality-agent.md` |

---

## P1 — Tham khảo khi mở rộng

| Source | URL | Reuse pattern |
|--------|-----|---------------|
| **Astra theme** | https://github.com/brainstormforce/astra | CartFlows ecosystem, fast WP base |
| **Inspiro Starter Sites** | https://github.com/wpzoom/inspiro-starter-sites | One-click Elementor + Woo demos (dark: Persona Lite) |
| **Elementor automation (DEV)** | https://dev.to/martijn_assie_12a2d3b1833/wordpress-page-builder-automation-generate-layouts-via-scripts-2ghc | JSON template → `wp_insert_post` loop |
| **Clone-and-mutate (DEV)** | https://dev.to/royal_plugins/four-architectures-for-letting-claude-edit-elementor-and-why-we-shipped-clone-and-mutate-11gi | Regenerate element IDs before save |
| **Respira Elementor bug** | https://github.com/respira-press/Respira.press-Documentation-and-Community/issues/18 | Always `wp_slash(wp_json_encode())` on save |
| **WooCommerce demo gen** | https://github.com/woocommerce/woocommerce/tree/trunk/plugins/woocommerce/client/admin/docs/features | Product CRUD classes |

---

## P2 — Không clone, chỉ học pattern

| Source | Why skip full clone |
|--------|---------------------|
| Premium FunnelKit template packs | License-bound; import via plugin UI |
| Elementor Pro template kits | Paid; use our `elementor-alpha-elite-homepage.json` |
| Full starter site importers | Overwrites site; conflicts with Alpha Elite copy |

---

## Mechanism extraction

### 1. Elementor page without wp-admin
```text
wp_load.php → wp_insert_post → update_post_meta(_elementor_data, wp_slash(json))
→ update_option(page_on_front) → flush_rewrite_rules
```
Source: StackOverflow + Elementor core + `ae-setup-once.php`

### 2. WooCommerce products without wp-admin
```text
wp_load.php → wc_get_product_id_by_sku → WC_Product_Simple → set_sku/price → save
```
Source: WooCommerce CRUD + WC-CLI field map

### 3. FunnelKit checkout without custom build
```text
FunnelKit → Funnels → Import template (Courselog / Magnetic / dark)
→ bind AE-APP-001 → thank-you + Telegram dynamic tag
```
Source: FunnelKit Elementor docs — **do not build checkout from scratch**

### 4. Agent harness (future)
```text
elementor-mcp import-template → compliance-agent scan → human G3 publish
```
Source: msrbuilds/elementor-mcp + `.ai/agents/funnelkit-agent.md`

---

## Install commands (skills, not WP plugins)

```bash
npx skills add coreyhaines31/marketingskills \
  --skill page-cro form-cro copywriting pricing-strategy

npx skills add addyosmani/web-quality-skills \
  --skill web-quality-audit performance core-web-vitals
```

---

## Acceptance

- [ ] Every automation script uses `wp_slash` on `_elementor_data`
- [ ] SKUs match `docs/offer_stack.md`
- [ ] FunnelKit flows use built-in Elementor checkout templates first
- [ ] No full theme/demo import that wipes Alpha Elite copy
