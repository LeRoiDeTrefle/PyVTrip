# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

This is the main file for the program PyVTrip
this program was made as a road planner for Electrical 
Vehicles.

This is currently a work in progress and might be highly unstable
Use with caution

Author: Boris Burgarella, Ph. D.



"""
from PyQt5 import QtWidgets
import sys, os
from GUI.MainWindow import Ui
import geocoder
 

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    window = Ui() # Create an instance of our class
    app.exec_() # Start the application