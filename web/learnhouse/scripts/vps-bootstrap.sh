#!/usr/bin/env bash
# LearnHouse production bootstrap - run on VPS (Ubuntu) as root
# Usage: bash vps-bootstrap.sh
set -euo pipefail

DOMAIN="${LEARNHOUSE_DOMAIN:-learn.hoa-homes.com}"
ADMIN_EMAIL="${LEARNHOUSE_ADMIN_EMAIL:-admin@hoa-homes.com}"
ADMIN_PASSWORD="${LEARNHOUSE_ADMIN_PASSWORD:-AlphaElite-Prod-Learn-2026!}"
ORG_NAME="${LEARNHOUSE_ORG_NAME:-Alpha Elite}"
ORG_SLUG="${LEARNHOUSE_ORG_SLUG:-alpha-elite}"
INSTALL_DIR="${LEARNHOUSE_INSTALL_DIR:-/opt/learnhouse}"

echo "=== LearnHouse VPS bootstrap: ${DOMAIN} ==="

export DEBIAN_FRONTEND=noninteractive
APT_OPTS='-y -qq -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold'
apt-get update -qq
apt-get upgrade $APT_OPTS
apt-get install $APT_OPTS curl git ca-certificates

if ! command -v docker >/dev/null 2>&1; then
  curl -fsSL https://get.docker.com | sh
fi
systemctl enable docker
systemctl start docker

if ! command -v node >/dev/null 2>&1 || [[ "$(node -v | cut -d. -f1 | tr -d v)" -lt 18 ]]; then
  curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
  apt-get install $APT_OPTS nodejs
fi

if command -v ufw >/dev/null 2>&1; then
  ufw allow 22/tcp 2>/dev/null || true
  ufw allow 80/tcp 2>/dev/null || true
  ufw allow 443/tcp 2>/dev/null || true
  ufw allow 24700/tcp 2>/dev/null || true
  ufw --force enable 2>/dev/null || true
fi

mkdir -p "${INSTALL_DIR}"
cd "${INSTALL_DIR}"

if [[ ! -f "${INSTALL_DIR}/learnhouse.config.json" ]]; then
  npx learnhouse@latest setup --ci \
    --install-dir "${INSTALL_DIR}" \
    --domain "${DOMAIN}" \
    --port 80 \
    --admin-email "${ADMIN_EMAIL}" \
    --admin-password "${ADMIN_PASSWORD}" \
    --org-name "${ORG_NAME}" \
    --org-slug "${ORG_SLUG}"
else
  echo "Existing install found - starting services..."
fi

npx learnhouse@latest start
sleep 15
npx learnhouse@latest doctor

cat > "${INSTALL_DIR}/PRODUCTION-CREDENTIALS.txt" <<EOF
URL:      https://${DOMAIN}
Email:    ${ADMIN_EMAIL}
Password: ${ADMIN_PASSWORD}
Org slug: ${ORG_SLUG}
EOF
chmod 600 "${INSTALL_DIR}/PRODUCTION-CREDENTIALS.txt"

echo ""
echo "=== DONE ==="
echo "URL:      https://${DOMAIN}"
echo "Email:    ${ADMIN_EMAIL}"
echo "Password: (saved in ${INSTALL_DIR}/PRODUCTION-CREDENTIALS.txt)"
echo "Run seed from Windows: .\\scripts\\deploy-production.ps1 -SeedOnly"
