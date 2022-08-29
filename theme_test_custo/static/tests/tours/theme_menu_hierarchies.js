/** @odoo-module */

import wTourUtils from 'website.tour_utils';

wTourUtils.registerEditionTour('theme_menu_hierarchies', {
    url: '/',
    test: true,
}, [
    {
        content: 'Check Mega Menu is correctly created',
        trigger: '#top_menu a.o_mega_menu_toggle',
    }, {
        content: 'Check Mega Menu content',
        trigger: '#top_menu div.o_mega_menu.show .fa-cube',
        run: () => null, // It's a check.
    }, {
        content: 'Check new top level menu is correctly created',
        trigger: '#top_menu .nav-item.dropdown:contains("Example 1")',
    }, {
        content: 'Check sub menu are correctly created',
        trigger: '#top_menu .dropdown-menu.show a.dropdown-item:contains("Item 1")',
        run: () => null, // It's a check.
    }, {
        content: 'The new menu hierarchy should not be included in the navbar',
        trigger: 'body:not(:has(#top_menu a[href="/dogs"]))',
        run: () => null, // It's a check.
    }, {
        content: 'The new menu hierarchy should be inside the footer',
        trigger: 'footer ul li a[href="/dogs"]',
        run: () => null, // It's a check.
    },
    wTourUtils.clickOnEdit(),
    {
        content: 'Click on footer',
        trigger: 'footer',
    }, {
        content: 'The theme custom footer template should be listed and selected',
        trigger: 'we-select[data-variable="footer-template"] we-toggler img[src*="/theme_test_custo"]',
        // TODO: this extra_trigger should be part of the `clickOnEdit` util
        extra_trigger: "#oe_snippets.o_loaded",
        run: () => null, // It's a check.
    }, {
        content: 'Click on header',
        trigger: 'header',
    }, {
        content: 'The theme custom header template should be listed and selected',
        trigger: 'we-select[data-variable="header-template"] we-toggler img[src*="/theme_test_custo"]',
        run: () => null, // It's a check.
    },
]);
