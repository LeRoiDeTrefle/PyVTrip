#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is used to store a class
specifically made to describe a place.

"""
import geocoder

class PlaceOb:
    
    def __init__(self,geocoderObject,Label=None,HTMLLabel=None):
        # geocoder info on this place
        self.geo = geocoderObject
        # Label of the place
        self.Label = Label
        self.HTMLLabel = HTMLLabel
        
        
    def HTML_Code(self):
        """
        returns the html code
        to add a marker on the map corresponding to itself
        """
        
        HTML_Code = ""
        HTML_Code += 'var marker{} = L.marker({}).addTo(map);\n'.format(self.HTMLLabel,self.geo.latlng)
        HTML_Code += 'marker{}.bindPopup("{}");\n'.format(self.HTMLLabel,self.Label)
        return HTML_Code
    

def From_ip():
    """
    this function can be called to get the info
    on the current position of the user based on 
    his/her IP adress
    """
    geo_info = geocoder.ip('me') # Gets the data from google about the current ip adress
    CurrentPos = PlaceOb(geo_info,Label="Current Position (based on your IP adress)",HTMLLabel="CurPos") # Creates the corresponding place object
    
    return CurrentPos