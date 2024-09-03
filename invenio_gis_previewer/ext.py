# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Vicky Rampin and New York University.
#
# invenio-gis-previewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for interacting with GeoServer in order to render GIS data."""

from flask_babelex import gettext as _
from invenio_drafts_resources.services import RecordService, RecordServiceConfig
from invenio_records_resources.services import FileService

from . import config
from .config import GISFileRecordServiceConfig
from .views import blueprint


class InvenioGISPreviewer(object):
    """invenio-gis-previewer extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.init_services(app)
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

    def init_services(self, app):
        """Initialize service to send files to GeoServer."""
        # Services
        self.records_service = RecordService(
            RecordServiceConfig,
            files_service=FileService(GISFileRecordServiceConfig),
        )
