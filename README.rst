..
    Copyright (C) 2024 Vicky Rampin and New York University.

    invenio-gis-previewer is free software; you can redistribute it and/or
    modify it under the terms of the MIT License; see LICENSE file for more
    details.

=======================
 invenio-gis-previewer
=======================

.. image:: https://github.com/nyudlts/invenio-gis-previewer/workflows/CI/badge.svg
        :target: https://github.com/nyudlts/invenio-gis-previewer/actions?query=workflow%3ACI

.. image:: https://img.shields.io/github/tag/nyudlts/invenio-gis-previewer.svg
        :target: https://github.com/nyudlts/invenio-gis-previewer/releases

.. image:: https://img.shields.io/pypi/dm/invenio-gis-previewer.svg
        :target: https://pypi.python.org/pypi/invenio-gis-previewer

.. image:: https://img.shields.io/github/license/nyudlts/invenio-gis-previewer.svg
        :target: https://github.com/nyudlts/invenio-gis-previewer/blob/master/LICENSE

Invenio module for interacting with GeoServer in order to render GIS data.

# Creating the GIS previewer

Just to map it all out (ha ha ha), there are a few files that we should add to make a previewer and they should all be named the same (you'll see how I did it below):

- `invenio-previewer/extensions`: add the python file that makes up the meat and potatoes of your previewer (`gis.py`)
- `examples/demo_files/`: add demo data used in testing for previewers (`gis.zip`)
- `invenio-previewer/templates/invenio-previewer`: add HTML file that will be used to render in previewer box (`gis.html`)
- `invenio-previewer/static/css`: if needed, add a folder to hold a CSS file (`gis/gis.css`)
- `invenio-previewer/static/jss`: if needed, do the same as above, but for javascript (`js/gis.js`)
- added preferred previewers to invenio.cfg file in UltraViolet repo, see pull request

# Using the GIS previewer

1. Fork and clone UltraViolet and get development environment running

2. Fork and clone this repository

3. Use `pip uninstall invenio-previewer` to install the previously installed official version

4. Use `pip install -e <path>/invenio-previewer` to tell UltraViolet to use the local version of invenio-previewer (you will be developing on the local one).

5. Follow the instructions from the Invenio-RDM team: https://invenio-previewer.readthedocs.io/en/latest/usage.html#custom-previewer.
