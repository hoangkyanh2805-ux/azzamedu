#!/usr/bin/env bash
# Issue SSL for learn.alex-mentor.com and restore nginx after domain migrate.
set -euo pipefail

D=/root/.learnhouse/default
DOMAIN="${LEARNHOUSE_DOMAIN:-learn.alex-mentor.com}"
EMAIL="${ACME_EMAIL:-admin@hoa-homes.com}"
cd "$D"

echo "=== domain=$DOMAIN ==="
ufw allow 80/tcp 2>/dev/null || true
ufw allow 443/tcp 2>/dev/null || true
ufw reload 2>/dev/null || true
command -v certbot >/dev/null || { apt-get update -qq; DEBIAN_FRONTEND=noninteractive apt-get install -y -qq certbot; }
mkdir -p /var/www/certbot

# Ensure webroot mount
grep -q '/var/www/certbot' docker-compose.yml || \
  sed -i 's#      - ./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro#      - ./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro\n      - /var/www/certbot:/var/www/certbot:ro#' docker-compose.yml

echo "=== HTTP-only nginx for ACME ==="
cat > extra/nginx.prod.conf <<NGINX
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN;
    location /.well-known/acme-challenge/ { root /var/www/certbot; }
    client_max_body_size 6G;
    large_client_header_buffers 4 32k;
    location / {
        proxy_pass http://learnhouse-app:80;
        proxy_set_header Host \$http_host;
        proxy_set_header X-Forwarded-Host \$http_host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400s;
    }
}
NGINX

docker compose --progress plain up -d --force-recreate nginx
sleep 8
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'

if [[ ! -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ]] || \
   [[ "$(readlink -f /etc/letsencrypt/live/$DOMAIN/fullchain.pem 2>/dev/null || true)" == *"azzamedu"* ]]; then
  echo "=== issuing cert for $DOMAIN ==="
  # Remove broken/temp symlink dir if present so certbot can create real cert
  if [[ -L "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ]]; then
    rm -rf "/etc/letsencrypt/live/$DOMAIN"
  fi
  certbot certonly --webroot -w /var/www/certbot -d "$DOMAIN" \
    --non-interactive --agree-tos -m "$EMAIL" --force-renewal
fi

[[ -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ]] || { echo "CERT MISSING"; exit 1; }
echo "=== cert OK ==="
ls -la "/etc/letsencrypt/live/$DOMAIN"

echo "=== write SSL nginx ==="
cat > extra/nginx.prod.conf <<NGINX
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN;
    location /.well-known/acme-challenge/ { root /var/www/certbot; }
    location / { return 301 https://\$host\$request_uri; }
}
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;
    server_name $DOMAIN;

    ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;

    client_max_body_size 6G;
    large_client_header_buffers 4 32k;

    location / {
        proxy_pass http://learnhouse-app:80;
        proxy_set_header Host \$http_host;
        proxy_set_header X-Forwarded-Host \$http_host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 86400s;
    }
}
NGINX

# Force https in .env if needed
sed -i 's#^NEXT_PUBLIC_LEARNHOUSE_HTTPS=.*#NEXT_PUBLIC_LEARNHOUSE_HTTPS=true#' .env 2>/dev/null || true
grep -q '^NEXT_PUBLIC_LEARNHOUSE_HTTPS=' .env || echo 'NEXT_PUBLIC_LEARNHOUSE_HTTPS=true' >> .env

docker compose --progress plain up -d --force-recreate nginx
sleep 6
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
docker logs "$(docker ps --format '{{.Names}}' | grep nginx | head -1)" --tail 20 2>&1 || true

echo "=== verify ==="
curl -sI "http://$DOMAIN/" | sed -n '1,15p' || true
curl -skI "https://$DOMAIN/" | sed -n '1,15p' || true
curl -skL "https://$DOMAIN/" | grep -oE 'https?://[^" ]+' | grep -E 'azzamedu|alex-mentor|content|og:image|favicon' | sort -u | sed -n '1,40p' || true

echo "=== DONE HTTPS $DOMAIN ==="
