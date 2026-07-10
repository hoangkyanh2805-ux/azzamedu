#!/bin/bash
# Alpha Elite Telegram Mini App — install on LearnHouse VPS (OneDash terminal)
set -euo pipefail
REMOTE_ROOT="/var/www/alpha-elite-miniapp"
TMP="/tmp/ae-miniapp.tgz.b64"

echo "=== Alpha Elite Mini App install ==="
mkdir -p "$REMOTE_ROOT"
cat > "$TMP" << 'B64_EOF'
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
B64_EOF

base64 -d "$TMP" | tar -xzf - -C /tmp
rm -f "$TMP"
cp -a /tmp/miniapp/. "$REMOTE_ROOT/"
rm -rf /tmp/miniapp
echo "Files installed to $REMOTE_ROOT"

NGINX_CT=$(docker ps --format '{{.Names}}' | grep -i nginx | head -1 || true)
COMPOSE_DIR=""
if [ -n "$NGINX_CT" ]; then
  COMPOSE_DIR=$(docker inspect "$NGINX_CT" --format '{{index .Config.Labels "com.docker.compose.project.working_dir"}}' 2>/dev/null || true)
fi
if [ -z "$COMPOSE_DIR" ] || [ ! -f "$COMPOSE_DIR/docker-compose.yml" ]; then
  COMPOSE_DIR=$(find /root /opt /home -maxdepth 5 -name docker-compose.yml 2>/dev/null | head -1 | xargs dirname 2>/dev/null || true)
fi
echo "nginx: $NGINX_CT"
echo "compose: $COMPOSE_DIR"

if [ -z "$COMPOSE_DIR" ] || [ ! -f "$COMPOSE_DIR/extra/nginx.prod.conf" ]; then
  echo "WARN: nginx.prod.conf not found — add location /miniapp/ manually"
  exit 0
fi

CONF="$COMPOSE_DIR/extra/nginx.prod.conf"
if ! grep -q 'location /miniapp/' "$CONF"; then
  cp "$CONF" "$CONF.bak-miniapp-$(date +%s)"
  cat >> "$CONF" << 'NGINX_EOF'

    location /miniapp/ {
        alias /var/www/alpha-elite-miniapp/;
        index index.html;
    }
NGINX_EOF
  echo "Patched $CONF"
fi

if ! grep -q '/var/www/alpha-elite-miniapp' "$COMPOSE_DIR/docker-compose.yml" 2>/dev/null; then
  sed -i 's|./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro|./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro\n      - /var/www/alpha-elite-miniapp:/var/www/alpha-elite-miniapp:ro|' \
    "$COMPOSE_DIR/docker-compose.yml" || true
fi

cd "$COMPOSE_DIR"
docker compose up -d --force-recreate nginx
docker exec "$NGINX_CT" nginx -t
echo ""
echo "DONE: https://learn.azzamedu.com/miniapp/"
echo "Test: curl -sI https://learn.azzamedu.com/miniapp/ | head -5"
