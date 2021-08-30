# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Vicky Rampin and New York University.
#
# invenio-gis-previewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for interacting with GeoServer in order to render GIS data."""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from flask import Blueprint, render_template
from flask_babelex import gettext as _

blueprint = Blueprint(
    'invenio_gis_previewer',
    __name__,
    template_folder='templates',
    static_folder='static',
)
"""Blueprint used to register template and static folders."""

