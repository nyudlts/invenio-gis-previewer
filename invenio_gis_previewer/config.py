# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Vicky Rampin and New York University.
#
# invenio-gis-previewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module for interacting with GeoServer in order to render GIS data."""

from invenio_records_resources.services import FileServiceConfig

from invenio_gis_previewer.gis_file_processor import GeoServerUploader


# TODO: add necessary configurations

GEOSERVER_API_PREFIX = '/geoserver/rest/'
"""URL prefix to GeoServer API."""


class GISFileRecordServiceConfig(FileServiceConfig):
    file_processors = FileServiceConfig.file_processors + [
        GeoServerUploader(),
    ]
