# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Vicky Rampin and New York University.
#
# invenio-gis-previewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for interacting with GeoServer in order to render GIS data."""

from .ext import InvenioGISPreviewer
from .version import __version__

__all__ = ('__version__', 'InvenioGISPreviewer')
