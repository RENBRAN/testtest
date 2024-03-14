# -*- coding: utf-8 -*-
{
    'name': 'Contract Reports SP',
    'version': '17.0',
    'sequence': 0,
    'author': 'TaurusTech',
    'website': '',
    'depends': [
        'base', 'sale'],
    'data': [

        "views/base_layout.xml",
        "views/contract_report.xml",
        "views/sale_order.xml",
        "views/custom_layout.xml",
    ],
    'assets': {
        'web.assets_backend': [
            # 'web/static/src/xml/**/*',
            # 'web/static/src/css/style.css',
            # 'web/arabic_report/static/src/css/style.css',
        ],
        'web.assets_common': [
            # 'web/static/src/css/style.css',
            # 'arabic_report/static/src/css/style.css',
            # 'web/contract_report/static/src/css/style.css',
        ],
        'web.report_assets_common': [
            'contract_report/static/src/css/style.css',

        ]
    },
    'installable': True,
}
