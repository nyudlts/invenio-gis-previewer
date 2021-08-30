from urllib.parse import urljoin

import requests

file_name = 'gis.zip'
resource = 'invenio/datastores/test/file.shp'
headers = {'content-type': 'application/zip'}

request_url = urljoin('http://localhost:9090/geoserver/rest/workspaces/', resource)

with open(file_name, 'rb') as f:
    r = requests.put(
        request_url,
        data=f,
        headers=headers,
        auth=('admin', 'geoserver')
    )
