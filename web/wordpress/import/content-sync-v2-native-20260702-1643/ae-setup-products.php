<?php
/**
 * Alpha Elite — one-time WooCommerce product setup (no wp-admin).
 *
 * UPLOAD to WordPress root, then open:
 *   http://hoa-homes.com/ae-setup-products.php?key=alpha-elite-2026
 *
 * DELETE this file immediately after success.
 */

declare(strict_types=1);

const AE_PRODUCTS_KEY = 'alpha-elite-2026';

if (($_GET['key'] ?? '') !== AE_PRODUCTS_KEY) {
    http_response_code(403);
    exit('Forbidden — add ?key=alpha-elite-2026');
}

$wp_load = __DIR__ . '/wp-load.php';
if (!is_readable($wp_load)) {
    exit('wp-load.php not found. Upload to WordPress root (public_html).');
}

require_once $wp_load;

if (!function_exists('wc_get_product_id_by_sku')) {
    exit('WooCommerce not active. Activate WooCommerce first.');
}

header('Content-Type: text/plain; charset=utf-8');

$products = [
    [
        'sku'   => 'AE-APP-001',
        'name'  => 'Apprentice Operating Course',
        'price' => '297',
        'desc'  => 'Structured trading education — operating system, not signals.',
    ],
    [
        'sku'   => 'AE-VIP-MON',
        'name'  => 'VIP Private Desk — Monthly',
        'price' => '149',
        'desc'  => 'VIP membership — monthly billing (MVP: one-time).',
    ],
    [
        'sku'   => 'AE-VIP-YR',
        'name'  => 'VIP Private Desk — Annual',
        'price' => '1290',
        'desc'  => 'VIP membership — annual.',
    ],
    [
        'sku'   => 'AE-DWY-001',
        'name'  => 'DWY Bot & Broker Setup',
        'price' => '497',
        'desc'  => 'Done-with-you automation setup — order bump / upsell.',
    ],
];

foreach ($products as $row) {
    $sku = $row['sku'];
    $existing_id = wc_get_product_id_by_sku($sku);

    if ($existing_id) {
        $product = wc_get_product($existing_id);
        echo "UPDATE: {$sku} (ID {$existing_id})\n";
    } else {
        $product = new WC_Product_Simple();
        echo "CREATE: {$sku}\n";
    }

    $product->set_name($row['name']);
    $product->set_sku($sku);
    $product->set_regular_price($row['price']);
    $product->set_description($row['desc']);
    $product->set_status('publish');
    $product->set_catalog_visibility('visible');
    $product->set_virtual(true);
    $product->set_sold_individually(false);

    $id = $product->save();
    echo "  OK ID {$id} — \${$row['price']}\n";
}

echo "\n=== DONE ===\n";
echo "NEXT: DELETE ae-setup-products.php from server\n";
echo "NEXT: FunnelKit funnel → bind AE-APP-001 at checkout\n";
