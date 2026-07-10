#!/usr/bin/env bash
# Migrate the LearnHouse production domain in-place. Run ON THE VPS as root.
#
#   OLD_DOMAIN=learn.hoa-homes.com NEW_DOMAIN=learn.azzamedu.com bash migrate-domain.sh
#
# What it does:
#   1. Finds config files under the install dir that reference OLD_DOMAIN
#      (node_modules/.git excluded), backs each up, replaces OLD_DOMAIN -> NEW_DOMAIN.
#   2. Restarts LearnHouse and runs doctor.
# The course content lives in Postgres and is NOT touched.
set -euo pipefail

OLD_DOMAIN="${OLD_DOMAIN:-learn.hoa-homes.com}"
NEW_DOMAIN="${NEW_DOMAIN:-learn.azzamedu.com}"
INSTALL_DIR="${LEARNHOUSE_INSTALL_DIR:-/opt/learnhouse}"
TS="$(date +%Y%m%d-%H%M%S)"

echo "=== LearnHouse domain migration ==="
echo "install dir : ${INSTALL_DIR}"
echo "old domain  : ${OLD_DOMAIN}"
echo "new domain  : ${NEW_DOMAIN}"

[[ -d "${INSTALL_DIR}" ]] || { echo "ERROR: ${INSTALL_DIR} not found"; exit 1; }
cd "${INSTALL_DIR}"

OLD_ESC="${OLD_DOMAIN//./\\.}"

echo
echo "--- config files referencing ${OLD_DOMAIN} ---"
mapfile -t FILES < <(grep -rIl \
  --exclude-dir=node_modules --exclude-dir=.git --exclude='*.bak-*' \
  -- "${OLD_DOMAIN}" "${INSTALL_DIR}" 2>/dev/null || true)

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "(none found in files — domain may already be migrated or stored in DB only)"
else
  for f in "${FILES[@]}"; do
    cp "$f" "$f.bak-$TS"
    sed -i "s/${OLD_ESC}/${NEW_DOMAIN}/g" "$f"
    echo "updated: $f   (backup: $f.bak-$TS)"
  done
fi

echo
echo "--- restarting LearnHouse ---"
if ! npx learnhouse@latest restart 2>/dev/null; then
  npx learnhouse@latest stop || true
  npx learnhouse@latest start
fi
sleep 15
npx learnhouse@latest doctor || true

echo
echo "=== DONE — verify http://${NEW_DOMAIN} ==="
echo "NOTE: if the site still calls the old domain in the browser, the Next.js frontend was built"
echo "with NEXT_PUBLIC_LEARNHOUSE_DOMAIN baked in. In that case re-run setup to rebuild:"
echo "  npx learnhouse@latest setup --ci --install-dir ${INSTALL_DIR} --domain ${NEW_DOMAIN} --port 80 \\"
echo "    --admin-email <admin> --admin-password <pw> --org-name 'Alpha Elite' --org-slug alpha-elite"
