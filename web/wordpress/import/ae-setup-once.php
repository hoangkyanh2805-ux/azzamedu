<?php
/**
 * Alpha Elite — one-time setup (no wp-admin import needed).
 * Build stamp: 2026-07-02 16:24 +07
 *
 * UPLOAD to WordPress root (same folder as wp-config.php), then open in browser:
 *   http://hoa-homes.com/ae-setup-once.php?key=alpha-elite-2026
 *
 * DELETE this file immediately after success.
 */

declare(strict_types=1);

const AE_SETUP_KEY = 'alpha-elite-2026';

if (($_GET['key'] ?? '') !== AE_SETUP_KEY) {
    http_response_code(403);
    exit('Forbidden — add ?key=alpha-elite-2026');
}

$wp_load = __DIR__ . '/wp-load.php';
if (!is_readable($wp_load)) {
    exit('wp-load.php not found. Upload this file to WordPress root (public_html).');
}

require_once $wp_load;

if (!function_exists('wp_insert_post')) {
    exit('WordPress not loaded.');
}

header('Content-Type: text/plain; charset=utf-8');

$log = [];

function ae_log(string $msg): void
{
    global $log;
    $log[] = $msg;
    echo $msg . "\n";
}

// 1) Elementor must be active
if (!did_action('elementor/loaded') && !defined('ELEMENTOR_VERSION')) {
    ae_log('ERROR: Elementor plugin not active. Activate Elementor first via panel Login → Plugins.');
    exit(1);
}

// 2) Switch to Elementor child theme if present
$theme_slug = 'alpha-elite-child-elementor';
$theme = wp_get_theme($theme_slug);
if ($theme->exists()) {
    switch_theme($theme_slug);
    ae_log("OK: Theme activated -> {$theme_slug}");
} else {
    ae_log("WARN: Theme {$theme_slug} not found. Upload alpha-elite-child-elementor.zip first.");
}

// 3) Load Elementor JSON (upload next to this script)
$json_path = __DIR__ . '/elementor-alpha-elite-homepage.json';
if (!is_readable($json_path)) {
    $json_path = __DIR__ . '/wp-content/ae-import/elementor-alpha-elite-homepage.json';
}
if (!is_readable($json_path)) {
    ae_log('ERROR: elementor-alpha-elite-homepage.json not found. Upload next to ae-setup-once.php');
    exit(1);
}

$raw = file_get_contents($json_path);
$data = json_decode($raw, true);
if (!is_array($data) || empty($data['content'])) {
    ae_log('ERROR: Invalid Elementor JSON');
    exit(1);
}

// 4) Create or update Homepage page
$existing = get_page_by_title('Homepage', OBJECT, 'page');
if ($existing) {
    $page_id = (int) $existing->ID;
    ae_log("OK: Updating existing page ID {$page_id}");
} else {
    $page_id = (int) wp_insert_post([
        'post_title' => 'Homepage',
        'post_status' => 'publish',
        'post_type' => 'page',
    ]);
    if (!$page_id) {
        ae_log('ERROR: Could not create page');
        exit(1);
    }
    ae_log("OK: Created page ID {$page_id}");
}

// 5) Elementor meta
update_post_meta($page_id, '_elementor_edit_mode', 'builder');
update_post_meta($page_id, '_elementor_template_type', 'wp-page');
update_post_meta($page_id, '_elementor_version', defined('ELEMENTOR_VERSION') ? ELEMENTOR_VERSION : '3.0.0');
update_post_meta($page_id, '_elementor_data', wp_slash(wp_json_encode($data['content'])));
if (!empty($data['page_settings'])) {
    update_post_meta($page_id, '_elementor_page_settings', $data['page_settings']);
}
update_post_meta($page_id, '_wp_page_template', 'elementor_canvas');

// 6) Static front page
update_option('show_on_front', 'page');
update_option('page_on_front', $page_id);
update_option('blog_public', '1');

// 7) Flush rewrite
flush_rewrite_rules();

ae_log('');
ae_log('=== DONE ===');
ae_log("Homepage URL: " . home_url('/'));
ae_log("Edit URL: " . admin_url("post.php?post={$page_id}&action=elementor"));
ae_log('');
ae_log('NEXT:');
ae_log('1) DELETE ae-setup-once.php from server NOW');
ae_log('2) DELETE elementor-alpha-elite-homepage.json from server');
ae_log('3) Open homepage — login admin to see Edit with Elementor');
ae_log('4) Disable Coming Soon mode');
