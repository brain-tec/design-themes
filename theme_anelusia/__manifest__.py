{
    'name': 'Anelusia Theme',
    'description': 'Anelusia Fashion Theme',
    'category': 'Theme/Retail',
    'summary': 'Diversity, Fashions, Trends, Clothes, Shoes, Sports, Fitness, Stores',
    'sequence': 180,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_content.xml',
        'views/images_library.xml',

        'views/snippets/s_company_team.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_text_cover.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_references.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_showcase.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/anelusia_description.jpg',
        'static/description/anelusia_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_banner_default_image': '/theme_anelusia/static/src/img/snippets/s_banner.jpg',
        'website.library_image_10': '/theme_anelusia/static/src/img/snippets/library_image_03.jpg',
        'website.library_image_05': '/theme_anelusia/static/src/img/snippets/library_image_13.jpg',
        'website.library_image_08': '/theme_anelusia/static/src/img/snippets/library_image_14.jpg',
        'website.library_image_13': '/theme_anelusia/static/src/img/snippets/library_image_10.jpg',
        'website.library_image_03': '/theme_anelusia/static/src/img/snippets/library_image_05.jpg',
        'website.library_image_02': '/theme_anelusia/static/src/img/snippets/library_image_16.jpg',
        'website.s_media_list_default_image_1': '/theme_anelusia/static/src/img/snippets/s_media_list_1.jpg',
        'website.s_media_list_default_image_2': '/theme_anelusia/static/src/img/snippets/s_media_list_2.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_text_cover', 's_images_wall', 's_color_blocks_2', 's_references',
                     's_media_list', 's_company_team', 's_call_to_action'],
        # TODO In master, remove unused templates instead.
        '_': ['s_comparisons'],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-anelusia.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_anelusia/static/src/js/tour.js',
        ],
    }
}
