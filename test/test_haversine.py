# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:57:14 2019

@author: Radek
"""

import sys, os

#################### MAKE CHANGES HERE #########################
address = "localhost" # address of the database
user = "root" # your username
password = "" # your password
database = "pytestproject_testing" # your database name
table = "test_table" # table name to store names and numbers (default "TESTING")
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/..")) # path to testing file ("haversine.py")
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
    assert hv.calcDistance(cordCracow, cordParis) >= 1270 # correct output is ~1275, giving some error margin
    assert hv.calcDistance(cordCracow, cordParis) <= 1280
    assert hv.calcDistance(cordCracow, cordRome) >= 1065
    assert hv.calcDistance(cordCracow, cordRome) <= 1075
    assert hv.calcDistance(cordParis, cordRome) >= 1100
    assert hv.calcDistance(cordParis, cordRome) <= 1110
    assert hv.calcDistance(cordParis, cordRome) != 800 # wrong value