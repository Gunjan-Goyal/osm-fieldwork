"""For generating .mbtiles archive"""

from osm_fieldwork.basemapper import create_basemap_file
from tests.test_basemap import boundary


create_basemap_file(
    boundary= boundary,
    outfile="outreachy.mbtiles",
    zooms="12-15",
    source="esri",
)