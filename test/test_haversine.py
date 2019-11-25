# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:57:14 2019

@author: Radek
"""

import sys

#################### MAKE CHANGES HERE #########################
sys.path.insert(1, 'D:/Dokumenty/Studia/Master2/DevOps/PytestProject') # path to testing file ("haversine.py")
########################### END ###############################

#import testing module
import haversine as hv

def test_putData():
    assert hv.putData() == True # functions already tested in test_datab.py
    
def test_getData():
    assert hv.getData() != None # functions already tested in test_datab.py
    
def test_getCoords():
    assert hv.getCords(hv.getData(), "Cracow") != None # city coordinates were retrieved with success
    assert hv.getCords(hv.getData(), "Paris") != None # city coordinates were retrieved with success
    assert hv.getCords(hv.getData(), "Rome") != None # city coordinates were retrieved with success
    assert hv.getCords(hv.getData(), "Berlin") == None # no city in the data
    assert hv.getCords(hv.getData(), "") == None # no city provided
    assert hv.getCords([], "Paris") == None # no data provided
    
def test_calcDistance():
    cordCracow = hv.getCords(hv.getData(), "Cracow") # get coordinates of the city
    cordParis = hv.getCords(hv.getData(), "Paris")
    cordRome = hv.getCords(hv.getData(), "Rome")
    assert hv.calcDistance(cordCracow, cordParis) == "1275.37" # correct value
    assert hv.calcDistance(cordCracow, cordRome) == "1071.5" # correct value
    assert hv.calcDistance(cordParis, cordRome) == "1106.56" # correct value
    assert hv.calcDistance(cordParis, cordRome) != "923.56" # wrong value