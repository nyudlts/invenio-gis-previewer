# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Vicky Rampin and New York University.
#
# invenio-gis-previewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_gis_previewer import InvenioGISPreviewer


def test_version():
    """Test version import."""
    from invenio_gis_previewer import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioGISPreviewer(app)
    assert 'invenio-gis-previewer' in app.extensions

    app = Flask('testapp')
    ext = InvenioGISPreviewer()
    assert 'invenio-gis-previewer' not in app.extensions
    ext.init_app(app)
    assert 'invenio-gis-previewer' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to invenio-gis-previewer' in str(res.data)
