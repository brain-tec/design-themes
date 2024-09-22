/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_image_title',
        name: 'Image Title',
        groupName: "Images",
    },
    {
        id: 's_key_images',
        name: 'Key Images',
        groupName: "Columns",
    },
    {
        id: 's_pricelist_cafe',
        name: 'Pricelist cafe',
        groupName: "Content",
    },
    {
        id: 's_quotes_carousel',
        name: 'Quotes',
        groupName: "People",
    },
    {
        id: 's_quadrant',
        name: 'Quadrant',
        groupName: "Images",
    },
];

wTourUtils.registerThemeHomepageTour("bistro_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"default-22"'),
    ...wTourUtils.dragNDrop(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1]),
    ...wTourUtils.dragNDrop(snippets[2]),
    ...wTourUtils.clickOnSnippet(snippets[2]),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[3]),
    ...wTourUtils.dragNDrop(snippets[4]),
]);
