# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Vicky Rampin and New York University.
#
# invenio-gis-previewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for interacting with GeoServer in order to render GIS data."""

from flask_babelex import gettext as _

from . import config
from .views import blueprint


class InvenioGISPreviewer(object):
    """invenio-gis-previewer extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        # TODO: This is an example of translation string with comment. Please
        # remove it.
        # NOTE: This is a note to a translator.
        _('A translation string')
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.register_blueprint(blueprint)
        app.extensions['invenio-gis-previewer'] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if 'BASE_TEMPLATE' in app.config:
            app.config.setdefault(
                'INVENIO_GIS_PREVIEWER_BASE_TEMPLATE',
                app.config['BASE_TEMPLATE'],
            )
        for k in dir(config):
            if k.startswith('INVENIO_GIS_PREVIEWER_'):
                app.config.setdefault(k, getattr(config, k))
