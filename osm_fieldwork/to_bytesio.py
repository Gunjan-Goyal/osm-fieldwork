"""Conversion of a GeoJSON file to a BytesIO object for streamlined in-memory data processing."""

from io import BytesIO

def read_geojson_bytesio(file_path):
    with open(file_path, "rb") as geojson_file:
        boundary = geojson_file.read()  # read as a `bytes` object.
        boundary_bytesio = BytesIO(boundary)   # add to a BytesIO wrapper

    return boundary_bytesio