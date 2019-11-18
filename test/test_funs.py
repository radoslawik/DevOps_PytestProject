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
database = "devops" # your database name
table = "TESTING" # table name to store names and numbers (default "TESTING")
sys.path.insert(1, 'D:/Dokumenty/Studia/Master2/DevOps/PytestProject') # path to testing file ("funs.py")
########################### END ###############################

#import testing module
import funs


def test_testConnection():  
    assert funs.testConnection(address, user, password, "incorrect_db_name") == False # in case of wrong database name
    assert funs.testConnection(address, user, "incorrect_password", database) == False # in case of incorrect password
    assert funs.testConnection(address, "wrong_user", password, database) == False # in case of wrong login
    assert funs.testConnection("made_up_address", user, password, database) == False # in case of wrong database address
    assert funs.testConnection(address, user, password, database) == True # correct data
    
def test_createTable():  
    assert funs.createTable(address, user, password, database, table) == True # correct data
    assert funs.createTable(address, user, password, database, "") == False # empty table name
    
def test_insertIntoTable():
    assert funs.insertIntoTable(address, user, password, database, table, "Radoslaw", "1") == True # query executed with success
    assert funs.insertIntoTable(address, user, password, database, table, "Joe", "2") == True # query executed with success
    assert funs.insertIntoTable(address, user, password, database, table, "Sue", "3") == True # query executed with success
    assert funs.insertIntoTable(address, user, password, database, table, "Radoslaw", "integer") == False # second parameter is not an integer
    assert funs.insertIntoTable(address, user, password, database, table, "Radoslaw", "") == False # second parameter is not an integer
    
def test_selectFromTable():
    assert funs.selectFromTable(address, user, password, database, "") == False # no table specified
    assert funs.selectFromTable(address, user, password, database, table) == True # correct data
    


