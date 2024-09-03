from invenio_records_resources.services.files.processors import FileProcessor


class GeoServerUploader(FileProcessor):
    # See invenio_records_resources/services/files/processors/image.py

    def can_process(self, file_record):
        return True

    def process(self, file_record):
        with open('/tmp/gis.log', 'a') as fp:
            print("process(%r)", file=fp)
