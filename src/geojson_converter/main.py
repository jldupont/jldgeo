'''
Converts geojson FeatureCollection to Newline delimited geojson geometry features

Created on Apr. 23, 2019

@author: jldupont

Example geojson FeatureCollection object

{
"type": "FeatureCollection",
"name": "ON_LDU",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [
{ "type": "Feature", "properties": { "PCA_ID": 180000059, "POSTALCODE": "P0R1L0", "PROV": "ON", "MAF_ID": 3500025
23, "PREC_CODE": 2, "PCA_COUNT": 516, "DOM_PCA": 0, "MULTI_PC": 0, "DEL_M_ID": "LB0001", "LONGITUDE": -83.4425680
69900005, "LATITUDE": 46.289068144200002 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -83.4323
79699999956, 46.29642750000005 ], [ -83.432314099999985, 46.295825900000068 ], [ -83.4323528, 46.29552810000007 ]
, [ -83.4323506, 46.294731200000058 ], [ -83.432348399999967, 46.293962100000044 ], [ -83.432283299999938, 46.293
666500000029 ], [ -83.432166, 46.293363 ], ... ] ] ] } },

Algorithm:
* features start_array

* features.item start_map 
   ==> features.item.properties

* features.item end_map

'''
import click
import ijson

from fsm import GeojsonFsm

@click.command()
@click.option(
    '--inputfile'
    ,type=click.File('r')
    ,help="""File of geojson format containing a FeatureCollection object"""
)
def geojson_converter(inputfile):
    """
    The main entry point
    """
    parser = ijson.parse(inputfile)
    
    count = 1000
    f = GeojsonFsm()
    
    for prefix, event, value in parser:
        f.submitEvent(prefix, event, value)
        
        count-=1
        
        if count == 0:
            break
    

if __name__ == '__main__':
    geojson_converter()