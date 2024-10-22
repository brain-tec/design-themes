{
    'name': 'Clean Theme',
    'description': 'Clean Theme',
    'category': 'Theme/Services',
    'summary': 'Legal, Corporate, Business, Tech, Services',
    'sequence': 120,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/image_content.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_cta_card.xml',
        'views/snippets/s_accordion_image.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_striped_top.xml',
        'views/snippets/s_card_offset.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_company_team_grid.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_quotes_carousel_compact.xml',
        'views/snippets/s_unveil.xml',
        'views/snippets/s_numbers_showcase.xml',
        'views/snippets/s_key_benefits.xml',
        'views/snippets/s_pricelist_boxed.xml',
        'views/snippets/s_striped_center_top.xml',
        'views/snippets/s_big_number.xml',
        'views/snippets/s_image_frame.xml',
        'views/snippets/s_wavy_grid.xml',
        'views/snippets/s_shape_image.xml',
        'views/snippets/s_images_constellation.xml',
        'views/snippets/s_empowerment.xml',
        'views/snippets/s_numbers_boxed.xml',
        'views/snippets/s_company_team_card.xml',
        'views/snippets/s_numbers_framed.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/clean_description.jpg',
        'static/description/clean_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_image_text_default_image': '/theme_clean/static/src/img/content/image_content_20.jpg',
        'website.s_banner_default_image': '/theme_clean/static/src/img/backgrounds/bg_snippet_07.jpg',
        'website.s_text_image_default_image': '/theme_clean/static/src/img/content/image_content_19.jpg',
        'website.s_picture_default_image': '/theme_clean/static/src/img/content/image_content_21.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_banner', 's_color_blocks_2', 's_title', 's_text_image', 's_image_text', 's_numbers_showcase', 's_company_team', 's_accordion_image', 's_cta_card'], 
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-clean.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_clean/static/src/js/tour.js',
        ],
    }
}
