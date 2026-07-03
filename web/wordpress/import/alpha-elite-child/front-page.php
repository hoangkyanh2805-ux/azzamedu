<?php
/**
 * Front page — full HTML import from homepage-dark-gold.html (no manual Elementor build).
 *
 * @package Alpha_Elite_Child
 */

declare(strict_types=1);

$html_path = get_stylesheet_directory() . '/homepage-dark-gold.html';
if (!is_readable($html_path)) {
    status_header(500);
    echo 'Alpha Elite homepage asset missing. Re-upload child theme.';
    exit;
}

$html = file_get_contents($html_path);
$css_url = esc_url(get_stylesheet_directory_uri() . '/alpha-elite-tokens.css');
$home = esc_url(home_url('/'));

$replacements = [
    'href="alpha-elite-tokens.css"' => 'href="' . $css_url . '"',
    'href="gameplan-preview.html"' => 'href="' . esc_url(home_url('/gameplan')) . '"',
    'href="gameplan-thank-you.html"' => 'href="' . esc_url(home_url('/gameplan-thank-you')) . '"',
    'href="apprentice-preview.html"' => 'href="' . esc_url(home_url('/apprentice')) . '"',
    'href="vip-preview.html"' => 'href="' . esc_url(home_url('/vip')) . '"',
    'href="quant-desk-preview.html"' => 'href="' . esc_url(home_url('/quant-desk')) . '"',
    'href="homepage-dark-gold.html"' => 'href="' . $home . '"',
    'action="gameplan-thank-you.html"' => 'action="' . esc_url(home_url('/gameplan-thank-you')) . '"',
    '<a href="#" class="ae-logo-gold">' => '<a href="' . $home . '" class="ae-logo-gold">',
];

$html = str_replace(array_keys($replacements), array_values($replacements), $html);

// Strip legacy cyan preview link in footer.
$html = preg_replace(
    '#<p style="margin-top:12px">\s*<a href="homepage\.html">.*?</p>#s',
    '',
    $html
) ?? $html;

echo $html;
exit;
