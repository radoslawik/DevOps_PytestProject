# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:57:14 2019

@author: Radek
"""

import sys

#################### MAKE CHANGES HERE #########################
address = "localhost" # address of the database
user = "root" # your username
password = "" # your password
database = "pytestproject_testing" # your database name
table = "test_table" # table name to store names and numbers (default "TESTING")
sys.path.insert(1, 'D:/Dokumenty/Studia/Master2/DevOps/PytestProject') # path to testing file ("haversine.py")
########################### END ###############################

#import testing module
import haversine as hv

def test_putData():
    assert hv.putData(address, user, password, database, table) == True # functions already tested in test_datab.py
    
def test_getData():
    assert hv.getData(address, user, password, database, table) != None # functions already tested in test_datab.py
    
def test_getCoords():
    assert hv.getCords(hv.getData(address, user, password, database, table), "Cracow") != None # city coordinates were retrieved with success
    assert hv.getCords(hv.getData(address, user, password, database, table), "Paris") != None # city coordinates were retrieved with success
    assert hv.getCords(hv.getData(address, user, password, database, table), "Rome") != None # city coordinates were retrieved with success
    assert hv.getCords(hv.getData(address, user, password, database, table), "Berlin") == None # no city in the data
    assert hv.getCords(hv.getData(address, user, password, database, table), "") == None # no city provided
    assert hv.getCords([], "Paris") == None # no data provided
    
def test_calcDistance():
    cordCracow = hv.getCords(hv.getData(address, user, password, database, table), "Cracow") # get coordinates of the city
    cordParis = hv.getCords(hv.getData(address, user, password, database, table), "Paris")
    cordRome = hv.getCords(hv.getData(address, user, password, database, table), "Rome")
    assert hv.calcDistance(cordCracow, cordParis) == "1275.37" # correct value
    assert hv.calcDistance(cordCracow, cordRome) == "1071.5" # correct value
    assert hv.calcDistance(cordParis, cordRome) == "1106.56" # correct value
    assert hv.calcDistance(cordParis, cordRome) != "923.56" # wrong value