# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class Crawler(HttpCase):
    def test_01_menu_hierarchies(self):
        self.start_tour('/@/', "theme_menu_hierarchies", login='admin')
