# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Vicky Rampin and New York University.
#
# invenio-gis-previewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""

import shutil
import tempfile

import pytest
from flask import Flask
from flask_babelex import Babel

from invenio_gis_previewer import InvenioGISPreviewer
from invenio_gis_previewer.views import blueprint


@pytest.fixture(scope='module')
def celery_config():
    """Override pytest-invenio fixture.

    TODO: Remove this fixture if you add Celery support.
    """
    return {}


@pytest.fixture(scope='module')
def create_app(instance_path):
    """Application factory fixture."""
    def factory(**config):
        app = Flask('testapp', instance_path=instance_path)
        app.config.update(**config)
        Babel(app)
        InvenioGISPreviewer(app)
        app.register_blueprint(blueprint)
        return app
    return factory
