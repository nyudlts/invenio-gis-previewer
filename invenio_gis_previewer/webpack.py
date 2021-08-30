# -*- coding: utf-8 -*-

"""JS/CSS bundles for GIS Previewer."""

from __future__ import absolute_import, print_function

from invenio_assets.webpack import WebpackThemeBundle

previewer = WebpackThemeBundle(
    __name__,
    'assets',
    default='semantic-ui',
    themes={
        'semantic-ui': dict(
            entry={
                'gis_css': './css/invenio_gis_previewer/gis/ol.css',
                'gis_js': './js/invenio_gis_previewer/gis/ol.js',
            },
            dependencies={
                #TODO add openlayers versions
                # 'ol':
            }
        ),
    }
)
"""Bundle of webpack assets."""
