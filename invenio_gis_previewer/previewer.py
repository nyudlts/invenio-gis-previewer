# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Vicky Rampin and New York University.
#
# invenio-gis-previewer is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""GIS data previewer"""

from __future__ import absolute_import, print_function
from flask import render_template, current_app
import zipfile

from .proxies import current_previewer

previewable_extensions = ['zip']

def can_preview(file):
    """Determine if the given file can be previewed by its extension.
        :param file: The file to be previewed.
        :returns: Boolean
        """

    if file.has_extensions('.zip'):
        with file.open() as fp:
            zf = zipfile.ZipFile(fp)
            for elem in zf.namelist():
                if elem.endswith(('.shp', '.dbf', '.shx', '.proj')):
                    return True

    #TODO add support for other GIS formats like raster images and geojson

def preview(file):
    """Render appropriate template with embed flag.
        .. note::
            Any non .png image is treated as .jpg
        :param file: The file to be previewed.
        :returns: Template with the preview of the provided file.
        """

    return render_template(
        "invenio_gis_previewer/gis.html",
        file=file,
        js_bundles=current_previewer.js_bundles + ['gis_js.js'],
        css_bundles=current_previewer.css_bundles + ["gis_css.css"]
    )
