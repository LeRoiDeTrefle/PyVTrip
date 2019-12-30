#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
this file was made to gather all the classes and functions 
related to the main window


"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEnginePage
import os, sys
import geocoder
from Mapping import html_Generator as HTMLGen
from Mapping import Place
from Mapping.Trip import TripOb

class Ui(QtWidgets.QMainWindow):
    """
    This is the main window class,
    it includes all the necessary functions to make
    the program run smoothly
    
    """
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('GUI/MainWindow.ui', self) # Load the .ui file
        html = HTMLGen.Default_map()
        self.show() # Show the GUI
        self.Map_View.setHtml(html)
        self.Set_Dpt_Button.clicked.connect(self.Set_Departure)
        self.Set_Arr_Button.clicked.connect(self.Set_Arrival)
        self.Trip = TripOb()
        
    def Set_Departure(self):
        DptStr = unicode(self.Departure_Line.text())
        Dpt_info = geocoder.osm(DptStr)
        Dpt_Place = Place.PlaceOb(Dpt_info,Label="Departure",HTMLLabel="Dpt")
        self.Trip.Dpt = Dpt_Place
        html = HTMLGen.Dpt_Arr_Map(Dpt=self.Trip.Dpt,Arr=self.Trip.Arr)
        self.Map_View.setHtml(html)
        
    def Set_Arrival(self):
        ArrStr = unicode(self.Arrival_Line.text())
        Arr_info = geocoder.osm(ArrStr)
        Arr_Place = Place.PlaceOb(Arr_info,Label="Arrival",HTMLLabel="Arr")
        self.Trip.Arr = Arr_Place
        html = HTMLGen.Dpt_Arr_Map(Dpt=self.Trip.Dpt,Arr=self.Trip.Arr)
        self.Map_View.setHtml(html)