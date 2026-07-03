<?php
/**
 * Alpha Elite Child — minimal bootstrap.
 */

declare(strict_types=1);

add_action('wp_enqueue_scripts', function (): void {
    if (!is_front_page()) {
        return;
    }
    wp_enqueue_style(
        'alpha-elite-tokens',
        get_stylesheet_directory_uri() . '/alpha-elite-tokens.css',
        [],
        '1.0.0'
    );
});
