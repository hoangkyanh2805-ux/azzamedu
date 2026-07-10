#!/usr/bin/env bash
# Enable Let's Encrypt HTTPS for a community-edition LearnHouse (containerized nginx).
# Idempotent: gets the cert via webroot first, only switches nginx to SSL once the cert exists.
# Run ON THE VPS as root.
set -e

D=/root/.learnhouse/default
DOMAIN="${LEARNHOUSE_DOMAIN:-learn.azzamedu.com}"
EMAIL="${ACME_EMAIL:-admin@hoa-homes.com}"
NGINX_CT=learnhouse-nginx-9f55066e
cd "$D"

echo "=== domain=$DOMAIN email=$EMAIL ==="

echo "=== prereqs: ufw 443 + certbot + webroot ==="
ufw allow 443/tcp 2>/dev/null || true
ufw reload 2>/dev/null || true
command -v certbot >/dev/null || { apt-get update -qq; DEBIAN_FRONTEND=noninteractive apt-get install -y -qq certbot; }
mkdir -p /var/www/certbot

ts=$(date +%Y%m%d-%H%M%S)
cp extra/nginx.prod.conf "extra/nginx.prod.conf.bak-$ts"
cp docker-compose.yml "docker-compose.yml.bak-$ts"
cp .env ".env.bak-$ts"

echo "=== ensure webroot mount on nginx service ==="
grep -q '/var/www/certbot' docker-compose.yml || sed -i 's#      - ./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro#      - ./extra/nginx.prod.conf:/etc/nginx/conf.d/default.conf:ro\n      - /var/www/certbot:/var/www/certbot:ro#' docker-compose.yml

if [ ! -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ]; then
  echo "=== no cert yet: switch nginx to HTTP+ACME (site stays up) then issue cert ==="
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
  certbot certonly --webroot -w /var/www/certbot -d "$DOMAIN" --non-interactive --agree-tos -m "$EMAIL"
fi

[ -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ] || { echo "CERT MISSING - aborting"; exit 1; }
echo "=== cert present ==="

echo "=== write full SSL nginx config ==="
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
    client_body_buffer_size 32k;
    client_header_buffer_size 32k;

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
        proxy_send_timeout 86400s;
        proxy_connect_timeout 75s;
    }
}
NGINX

echo "=== compose: add 443 + letsencrypt mount ==="
grep -q '"443:443"' docker-compose.yml || sed -i 's#      - "${HTTP_PORT:-80}:80"#      - "${HTTP_PORT:-80}:80"\n      - "443:443"#' docker-compose.yml
grep -q '/etc/letsencrypt' docker-compose.yml || sed -i 's#      - /var/www/certbot:/var/www/certbot:ro#      - /var/www/certbot:/var/www/certbot:ro\n      - /etc/letsencrypt:/etc/letsencrypt:ro#' docker-compose.yml

echo "=== .env + config -> https (admin email untouched) ==="
sed -i 's#http://learn.azzamedu.com#https://learn.azzamedu.com#g; s#ws://learn.azzamedu.com#wss://learn.azzamedu.com#g; s/^NEXT_PUBLIC_LEARNHOUSE_HTTPS=False/NEXT_PUBLIC_LEARNHOUSE_HTTPS=True/' .env
sed -i 's/"useHttps": false/"useHttps": true/' learnhouse.config.json

echo "=== auto-renew deploy hook (reload containerized nginx) ==="
mkdir -p /etc/letsencrypt/renewal-hooks/deploy
cat > /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh <<'HOOK'
#!/bin/sh
docker exec learnhouse-nginx-9f55066e nginx -s reload 2>/dev/null || true
HOOK
chmod +x /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh

echo "=== apply (recreate all) ==="
docker compose --progress plain up -d --force-recreate
sleep 25
echo "--- nginx -t ---"
docker exec "$NGINX_CT" nginx -t
echo "--- containers ---"
docker ps --format '{{.Names}}  {{.Status}}'
echo "--- https health (local) ---"
curl -sk "https://127.0.0.1/api/v1/health" -H "Host: $DOMAIN"; echo
echo "=== ENABLE-HTTPS DONE ==="
