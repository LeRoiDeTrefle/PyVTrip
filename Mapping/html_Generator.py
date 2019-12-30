#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

This file will be used to generate the html code
in order to show the right map in the 
map tab

"""
import geocoder
from . import Place


def Default_map():
    
    """
    generates the code for the default printed map,
    gets the initial position from the current IP
    
    
    """
    # Create the current position place object
    CurrentPos = Place.From_ip()
    
    HTML_Code =  '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr">\n'
    HTML_Code += '<head>\n'
    HTML_Code += '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />\n'
    HTML_Code += '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" />\n'
    HTML_Code += '<script type="text/javascript" src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js"></script>\n'
    HTML_Code += '</head>\n'
    HTML_Code += '<body onload="initialize()">\n'
    HTML_Code += '<div id="map" style="width:100%; height:100%"></div>\n'
    HTML_Code += '</body>\n'
    HTML_Code += '</html>\n'
    HTML_Code += '<script type="text/javascript">\n'
    HTML_Code += 'function initialize() {\n'
    HTML_Code += '    var map = L.map("map").setView({}, 12); // LIGNE 14\n'.format(CurrentPos.geo.latlng)
    HTML_Code += 'var osmLayer = L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", { // LIGNE 16\n'
    HTML_Code += 'attribution: "© OpenStreetMap contributors",\n'
    HTML_Code += 'maxZoom: 19\n'
    HTML_Code += '});\n'
    HTML_Code += 'map.addLayer(osmLayer);\n'
    HTML_Code += CurrentPos.HTML_Code()
    HTML_Code += '}\n'
    HTML_Code += '</script>\n'
    
    return HTML_Code


def Dpt_Arr_Map(Dpt=None,Arr=None):
    """
    this function will update the map when the destination
    and departure are given by the user
    
    """

    # Create the current position place object
    CurrentPos = Place.From_ip()
    geo_info = geocoder.ip('me') # Gets the data from google about the current ip adress
    LatLong = geo_info.latlng
    
    HTML_Code =  '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr">\n'
    HTML_Code += '<head>\n'
    HTML_Code += '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />\n'
    HTML_Code += '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.1/dist/leaflet.css" />\n'
    HTML_Code += '<script type="text/javascript" src="https://unpkg.com/leaflet@1.3.1/dist/leaflet.js"></script>\n'
    HTML_Code += '</head>\n'
    HTML_Code += '<body onload="initialize()">\n'
    HTML_Code += '<div id="map" style="width:100%; height:100%"></div>\n'
    HTML_Code += '</body>\n'
    HTML_Code += '</html>\n'
    HTML_Code += '<script type="text/javascript">\n'
    HTML_Code += 'function initialize() {\n'
    HTML_Code += '    var map = L.map("map").setView({}, 12); // LIGNE 14\n'.format(LatLong)
    HTML_Code += 'var osmLayer = L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", { // LIGNE 16\n'
    HTML_Code += 'attribution: "© OpenStreetMap contributors",\n'
    HTML_Code += 'maxZoom: 19\n'
    HTML_Code += '});\n'
    HTML_Code += 'map.addLayer(osmLayer);\n'
    
    HTML_Code += CurrentPos.HTML_Code() 
    # first we see if the departure is already set
    if Dpt is not None:
        HTML_Code += Dpt.HTML_Code()
        
    # Then we do the same for the arrival 
    if Arr is not None:
        HTML_Code += Arr.HTML_Code()
    HTML_Code += '}\n'
    HTML_Code += '</script>\n'    

    return HTML_Code

if __name__=="__main__":
    print(Dpt_Arr_Map())