This folder contains several documents and test data files that can be used.

gis.zip is an archive that contains the shapefile and its component parts. The file is

New York City Real Estate Sales, 2015
Author: GIS Lab, Newman Library, Baruch CUNY
Description: This point layer was created from Detailed Annual Sales Reports by Borough published by New York City Department of Finance. It represents locations of all properties sold in New York City. Several Python scripts were written to read-in each borough's sales data and combine them into sales for New York City as whole. NYC Geoclient API, developed by NYC DOITT, was used in a script to geocode locations of the properties sold. Locations geocoded by the script were matched by property address or by property block and lot information, if the address was missing or incomplete. For some properties lot information has changed from the year of the property sale (e.g. lot has been split and renumbered) and doesn’t exist in the city's current property and address database. Manual matching was performed for those records by examining archival tax maps. Due to the vertical nature of the real estate market in New York, multiple points / transactions may coincide in the same location. The coordinate reference system for this layer is NY State Plane Long Island in feet. The unique identifier of the dataset is Sale_id. Bbl_id is a unique identifier for the property and may repeat in the dataset if the property was sold more than once in the same year. The user should be cautious of sales with values less than $10 or equal to $0, which are marked as non-usable in this dataset. These sales are transfers of property and are not considered representative of true market conditions. This layer was created as a part of the NYC Geocoded Real Estate Sales data series.

The layer is available via the SDR at https://geo.nyu.edu/catalog/nyu-2451-34678 and the Solr document is available as a JSON response at https://geo.nyu.edu/catalog/nyu-2451-34678.json

This file is good for your testing purposes for a couple of reasons. First, it is fairly large and users don't necessarily need to see every case displayed in order to get context for the file. Second, it is in NAD1983 Long Island State Plane coordinate reference system, which is not standard, and it will need to be converted to the standard WGS84 to work in Geoserver. The classic challenge is how to do "on the fly" conversions to publish into Geoserver and whether or not this is advisable. A lot can go wrong or cause errors in geoserver, including spaces in file names, irregular characters in the attribute table, and more.

If you want to experiment with just the viewer part itself and call from the web services alone, you can do that directly from:

https://maps-public.geo.nyu.edu/geoserver/sdr/wms?service=WMS&version=1.1.0&request=GetMap&layers=sdr:nyu_2451_34678&styles=&bbox=-74.2519836425781,40.4971008300781,-73.6980285644531,40.9142456054688&width=768&height=578&srs=EPSG:4326&format=application/openlayers

Other useful things and tools to know about:

Most people use GDAL and the org2ogr library to convert into WGS84 and to extract the essential info you would need to render the data. See https://gdal.org/programs/ogr2ogr.html

SDRfriend: a series of rake tasks that execute calls to GDAL and the ogr2ogr library for conversion to .sql files. It can be a help in modeling how to leverage the ogr2ogr library in the context of another application. See https://github.com/NYULibraries/sdrfriend

The closest thing I've heard of that mirrors this work is Princeton's Figgy end to end service. See https://pulibrary/figgy for more information.
