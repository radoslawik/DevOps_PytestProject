# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:57:14 2019

@author: Radek
"""

import sys, os

#################### MAKE CHANGES HERE #########################
default_address = "localhost" # address of the database
default_user = "root" # your username
default_password = "" # your password
database = "pytestproject_testing" # your database name
table = "test_table" # table name to store names and numbers (default "TESTING")
########################### END ###############################

#### CHECK THE ENVIRONMENTAL VARIABLES - DO NOT MODIFY ########
if os.environ.get('MYSQL_ADDRESS') is not None:
    address = os.environ['MYSQL_ADDRESS']
else:
    address = default_address 
    
if os.environ.get('MYSQL_USER') is not None:
    user = os.environ['MYSQL_USER']  
else:
    user = default_user 

if os.environ.get('MYSQL_PASS') is not None:
    password = os.environ['MYSQL_PASS']  
else:
    password = default_password 
###############################################################

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/..")) # path to testing file ("datab.py")
import datab #import testing module

def test_createDatabase():
    assert datab.createDatabase(address, user, password, database) == True # correct data
    assert datab.createDatabase(address, user, password, "") == False # incorrect database name
    assert datab.createDatabase(address, user, "incorrect_password", database) == False # in case of incorrect password
    assert datab.createDatabase(address, "wrong_user", password, database) == False # in case of wrong login
    assert datab.createDatabase("made_up_address", user, password, database) == False # in case of wrong database address

def test_testConnection():  
    assert datab.testConnection(address, user, password, "incorrect_db_name") == False # in case of wrong database name
    assert datab.testConnection(address, user, "incorrect_password", database) == False # in case of incorrect password
    assert datab.testConnection(address, "wrong_user", password, database) == False # in case of wrong login
    assert datab.testConnection("made_up_address", user, password, database) == False # in case of wrong database address
    assert datab.testConnection(address, user, password, database) == True # correct data
    
def test_createTable():  
    assert datab.createTable(address, user, password, database, table) == True # correct data
    assert datab.createTable(address, user, password, database, "") == False # empty table name
    
def test_insertIntoTable():
    assert datab.insertIntoTable(address, user, password, database, table, "Paris", "48.85", "2.35") == True # query executed with success
    assert datab.insertIntoTable(address, user, password, database, table, "Rome", "41.89", "12.51") == True # query executed with success 
    assert datab.insertIntoTable(address, user, password, database, table, "Cracow", "50.04", "19.94") == True # query executed with success 
    assert datab.insertIntoTable(address, user, password, database, table, "Berlin", "integer", "2") == False # second parameter is not decimal
    assert datab.insertIntoTable(address, user, password, database, table, "Rio", "", "30.20") == False # second parameter is not decimal
    assert datab.insertIntoTable(address, user, password, database, table, "Rio", "9999.99", "30.20") == False # second parameter is too big
    
def test_selectFromTable():
    assert datab.selectFromTable(address, user, password, database, "") == None # no table specified
    assert datab.selectFromTable(address, user, password, database, table) != None # correct data
    


