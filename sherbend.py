#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" """

import fiona

from shapely import LineString

# Read Options

in_file = 'test.gpkg'
with fiona.open (in_file, 'r') as source:
    crs = source.crs
    driver = source.driver
    schema = source.schema

    for feature in source:
        try:
            geom = feature['geometry']
            properties = feature['properties']
            type = geom['type']
            coords = geom['coordinates']
            if type = 'LineString':
                shapely_feature = LineString(coords)

        except Exception, e:
            print ("Error processing feature) {0}".format(feature['id']))



