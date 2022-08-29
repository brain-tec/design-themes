{
    'name': 'Custom Theme (Testing suite)',
    'summary': '',
    'description': '',
    'category': 'Theme/Testing',
    'version': '15.0.0',
    'depends': ['website'],
    'data': [
        'data/images.xml',
        'data/menu.xml',
        'data/pages.xml',
        'views/footer.xml',
        'views/header.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            'theme_test_custo/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'theme_test_custo/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_tests': [
            'theme_test_custo/static/tests/tours/**/*',
        ],
    },
    'license': 'LGPL-3',
}
