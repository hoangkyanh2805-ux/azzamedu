#!/usr/bin/env bash
# Fix LearnHouse domain on alex-mentor clone. Install lives in /root/.learnhouse/default
set -euo pipefail

OLD_DOMAIN="${OLD_DOMAIN:-learn.azzamedu.com}"
NEW_DOMAIN="${NEW_DOMAIN:-learn.alex-mentor.com}"
OLD_TOP="${OLD_TOP:-azzamedu.com}"
NEW_TOP="${NEW_TOP:-alex-mentor.com}"
INSTALL="${LEARNHOUSE_INSTALL_DIR:-/root/.learnhouse/default}"
TS="$(date +%Y%m%d-%H%M%S)"

echo "=== Fix ${OLD_DOMAIN} -> ${NEW_DOMAIN} ==="
echo "install: ${INSTALL}"
[[ -d "${INSTALL}" ]] || { echo "MISSING ${INSTALL}"; exit 1; }
cd "${INSTALL}"

echo
echo "--- 1) Backup + replace config ---"
for f in .env learnhouse.config.json extra/nginx.prod.conf docker-compose.yml; do
  if [[ -f "$f" ]]; then
    cp "$f" "$f.bak-$TS"
    sed -i "s/${OLD_DOMAIN//./\\.}/${NEW_DOMAIN}/g" "$f"
    sed -i "s/${OLD_TOP//./\\.}/${NEW_TOP}/g" "$f"
    echo "updated $f"
  else
    echo "missing $f"
  fi
done

echo "--- domain lines in .env ---"
grep -Ei 'DOMAIN|URL|COOKIE|NEXTAUTH|COLLAB' .env | sed -E 's/(PASSWORD|SECRET|KEY|TOKEN).*/\1***/I' || true

echo
echo "--- 2) Content volume ---"
VOL=/var/lib/docker/volumes/learnhouse-9f55066e_learnhouse_content_9f55066e/_data
if [[ -d "$VOL" ]]; then
  du -sh "$VOL"
  echo "file count: $(find "$VOL" -type f | wc -l)"
  ls -la "$VOL" | head -25
else
  echo "CONTENT VOLUME MISSING: $VOL"
fi

echo
echo "--- 3) Recreate stack with new env ---"
docker compose up -d --force-recreate
sleep 20
docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'

APP=$(docker ps --format '{{.Names}}' | grep learnhouse-app | head -1)
DB=$(docker ps --format '{{.Names}}' | grep learnhouse-db | head -1)
echo "APP=$APP DB=$DB"

echo
echo "--- 4) App env check ---"
docker exec "$APP" sh -c 'env | grep -Ei "DOMAIN|NEXTAUTH_URL|BACKEND|COOKIE|COLLAB|TOP" | sort'

echo
echo "--- 5) Postgres URL replace ---"
DB_USER=$(grep -E '^POSTGRES_USER=' .env | cut -d= -f2- || true)
DB_NAME=$(grep -E '^POSTGRES_DB=' .env | cut -d= -f2- || true)
DB_USER=${DB_USER:-learnhouse}
DB_NAME=${DB_NAME:-learnhouse}

docker exec -i "$DB" psql -U "$DB_USER" -d "$DB_NAME" <<SQL
DO \$\$
DECLARE
  r RECORD;
  n bigint;
BEGIN
  FOR r IN
    SELECT c.table_schema, c.table_name, c.column_name, c.data_type
    FROM information_schema.columns c
    JOIN information_schema.tables t
      ON t.table_schema=c.table_schema AND t.table_name=c.table_name
    WHERE c.table_schema='public'
      AND t.table_type='BASE TABLE'
      AND c.data_type IN ('text','character varying','json','jsonb')
  LOOP
    BEGIN
      IF r.data_type IN ('json','jsonb') THEN
        EXECUTE format('SELECT count(*) FROM %I.%I WHERE %I::text LIKE %L', r.table_schema, r.table_name, r.column_name, '%${OLD_DOMAIN}%') INTO n;
        IF n > 0 THEN
          RAISE NOTICE 'json %.% rows=%', r.table_name, r.column_name, n;
          EXECUTE format('UPDATE %I.%I SET %I = replace(%I::text, %L, %L)::%s WHERE %I::text LIKE %L',
            r.table_schema, r.table_name, r.column_name, r.column_name, '${OLD_DOMAIN}', '${NEW_DOMAIN}', r.data_type, r.column_name, '%${OLD_DOMAIN}%');
        END IF;
        EXECUTE format('SELECT count(*) FROM %I.%I WHERE %I::text LIKE %L', r.table_schema, r.table_name, r.column_name, '%${OLD_TOP}%') INTO n;
        IF n > 0 THEN
          RAISE NOTICE 'json-top %.% rows=%', r.table_name, r.column_name, n;
          EXECUTE format('UPDATE %I.%I SET %I = replace(%I::text, %L, %L)::%s WHERE %I::text LIKE %L',
            r.table_schema, r.table_name, r.column_name, r.column_name, '${OLD_TOP}', '${NEW_TOP}', r.data_type, r.column_name, '%${OLD_TOP}%');
        END IF;
      ELSE
        EXECUTE format('SELECT count(*) FROM %I.%I WHERE %I LIKE %L', r.table_schema, r.table_name, r.column_name, '%${OLD_DOMAIN}%') INTO n;
        IF n > 0 THEN
          RAISE NOTICE 'text %.% rows=%', r.table_name, r.column_name, n;
          EXECUTE format('UPDATE %I.%I SET %I = replace(%I, %L, %L) WHERE %I LIKE %L',
            r.table_schema, r.table_name, r.column_name, r.column_name, '${OLD_DOMAIN}', '${NEW_DOMAIN}', r.column_name, '%${OLD_DOMAIN}%');
        END IF;
        EXECUTE format('SELECT count(*) FROM %I.%I WHERE %I LIKE %L', r.table_schema, r.table_name, r.column_name, '%${OLD_TOP}%') INTO n;
        IF n > 0 THEN
          RAISE NOTICE 'text-top %.% rows=%', r.table_name, r.column_name, n;
          EXECUTE format('UPDATE %I.%I SET %I = replace(%I, %L, %L) WHERE %I LIKE %L',
            r.table_schema, r.table_name, r.column_name, r.column_name, '${OLD_TOP}', '${NEW_TOP}', r.column_name, '%${OLD_TOP}%');
        END IF;
      END IF;
    EXCEPTION WHEN OTHERS THEN
      RAISE NOTICE 'skip %.%: %', r.table_name, r.column_name, SQLERRM;
    END;
  END LOOP;
END
\$\$;
SQL

echo
echo "--- 6) Homepage asset hosts ---"
curl -skL "https://${NEW_DOMAIN}/" 2>/dev/null | grep -oE 'https?://[^"'\'' ]+' | grep -E 'azzamedu|alex-mentor|og:image|favicon|content|media' | sort -u | head -50 || true
echo "--- remaining install refs ---"
grep -rIl --exclude='*.bak-*' --exclude-dir=node_modules -- "${OLD_DOMAIN}" "${INSTALL}" 2>/dev/null || echo none

echo
echo "=== DONE ==="
echo "Hard refresh https://${NEW_DOMAIN}/"
echo "If SSL warns: cert still for ${OLD_DOMAIN} — issue new cert for ${NEW_DOMAIN}"
