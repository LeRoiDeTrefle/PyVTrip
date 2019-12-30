# -*- coding: utf-8 -*-

"""
this file was made to gather all the classes and functions 
related to the main window


"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEnginePage
import os, sys
from Mapping import html_Generator as HTMLGen

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('GUI/MainWindow.ui', self) # Load the .ui file
        html = HTMLGen.Default_map()
        self.show() # Show the GUI
        self.Map_View.setHtml(html)