<?php
/**
 * Alpha Elite Child (Elementor mode) — enqueue design tokens only.
 */

declare(strict_types=1);

add_action('wp_enqueue_scripts', function (): void {
    wp_enqueue_style(
        'alpha-elite-tokens',
        get_stylesheet_directory_uri() . '/alpha-elite-tokens.css',
        [],
        '1.1.0'
    );
    wp_enqueue_style(
        'alpha-elite-homepage-sections',
        get_stylesheet_directory_uri() . '/homepage-sections.css',
        ['alpha-elite-tokens'],
        '1.1.0'
    );
});
