{
    'name': 'Loftspace Theme',
    'description': 'Loftspace Fashion Theme',
    'category': 'Theme/Retail',
    'summary': 'Furniture, Toys, Games, Kids, Boys, Girls, Stores',
    'sequence': 130,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_content.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_striped_top.xml',
        'views/snippets/s_card_offset.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_comparisons_horizontal.xml',
        'views/snippets/s_sidegrid.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_cards_grid.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_image_title.xml',
        'views/snippets/s_images_mosaic.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_pricelist_boxed.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_company_team_shapes.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_features_wall.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel_minimal.xml',
        'views/snippets/s_unveil.xml',
        'views/snippets/s_key_benefits.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_carousel_intro.xml',
        'views/snippets/s_striped_center_top.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_quadrant.xml',
        'views/snippets/s_striped.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_faq_collapse.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_big_number.xml',
        'views/snippets/s_wavy_grid.xml',
        'views/snippets/s_text_cover.xml',
        'views/snippets/s_empowerment.xml',
        'views/snippets/s_numbers_boxed.xml',
        'views/snippets/s_company_team_card.xml',
        'views/snippets/s_split_intro.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/loftspace_description.jpg',
        'static/description/loftspace_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_image_text_default_image': '/theme_loftspace/static/src/img/snippets/s_image_text.jpg',
        'website.s_product_list_default_image_1': '/theme_loftspace/static/src/img/snippets/s_product_1.jpg',
        'website.s_picture_default_image': '/theme_loftspace/static/src/img/snippets/s_picture.jpg',
        'website.s_media_list_default_image_1': '/theme_loftspace/static/src/img/snippets/s_media_list_1.jpg',
        'website.s_media_list_default_image_2': '/theme_loftspace/static/src/img/snippets/s_media_list_2.jpg',
        'website.s_text_image_default_image': '/theme_loftspace/static/src/img/snippets/s_text_image.jpg',
        'website.s_cta_box_default_image': '/theme_loftspace/static/src/img/content/s_cta_box_default_image.jpg',
        'website.s_three_columns_default_image_3': '/theme_loftspace/static/src/img/snippets/library_image_07.jpg',
        'website.library_image_03': '/theme_loftspace/static/src/img/snippets/s_images_wall_01.jpg',
        'website.library_image_02': '/theme_loftspace/static/src/img/snippets/s_images_wall_05.jpg',
        'website.library_image_10': '/theme_loftspace/static/src/img/snippets/s_images_wall_06.jpg',
        'website.library_image_05': '/theme_loftspace/static/src/img/snippets/s_images_wall_02.jpg',
        'website.library_image_07': '/theme_loftspace/static/src/img/snippets/library_image_07.jpg',
        'website.library_image_16': '/theme_loftspace/static/src/img/snippets/s_images_wall_04.jpg',
        'website.library_image_13': '/theme_loftspace/static/src/img/snippets/s_images_wall_03.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_banner', 's_text_block', 's_striped', 's_key_images', 's_features', 's_quotes_carousel', 's_faq_collapse', 's_cta_box',],
    },
    'new_page_templates': {
        'about': {
            'personal': ['s_text_cover', 's_image_text', 's_text_block_h2', 's_numbers', 's_features', 's_call_to_action'],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-loftspace.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_loftspace/static/src/js/tour.js',
        ],
    }
}
