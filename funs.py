# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:55:58 2019

@author: Radek
"""

import pymysql

def testConnection(address, username, password, database): 
    try:
        #open database connection 
        conn = pymysql.connect(address, username, password, database)
        # prepare a cursor object using cursor() method
        cursor = conn.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        data = cursor.fetchone()
        print ("Database version: %s " % data)
        # disconnect from server
        conn.close()
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except:
        return False
        
    return True
    
def createTable(address, username, password, database, table):
    try:
        # Open database connection
        conn = pymysql.connect(address, username, password, database)
        # prepare a cursor object using cursor() method
        cursor = conn.cursor()
        # Drop table if it already exist using execute() method.
        check_command = "DROP TABLE IF EXISTS " + table;
        cursor.execute(check_command)
        # Create table as per requirement
        command = "CREATE TABLE " + table + "(NAME  VARCHAR(30) NOT NULL, NUMBER INT)"
        cursor.execute(command)
        # disconnect from server
        conn.close()
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except:
        return False
        
    return True
    
def createTable(address, username, password, database, table):

    command = "CREATE TABLE " + table + "(NAME  VARCHAR(30) NOT NULL, NUMBER INT)"
    try:
        # Open database connection
        conn = pymysql.connect(address, username, password, database)
        # prepare a cursor object using cursor() method
        cursor = conn.cursor()
        # Drop table if it already exist using execute() method.
        check_command = "DROP TABLE IF EXISTS " + table;
        cursor.execute(check_command)
        cursor.execute(command)
        # disconnect from server
        conn.close()
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except:
        return False
        
    return True
    
def insertIntoTable(address, username, password, database, table, name, number):

    command = "INSERT INTO " + table + "(NAME, NUMBER) VALUES('" + name + "', " + number + ")"
    try:
        # Open database connection
        conn = pymysql.connect(address, username, password, database)
        # prepare a cursor object using cursor() method
        cursor = conn.cursor()
        cursor.execute(command)
        # disconnect from server
        conn.close()
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except:
        return False
        
    return True
    
def main():
    if(testConnection("localhost","root","","devops")):
        print("Connection tested with success")
    if(createTable("localhost","root","","devops", "TESTING")):
        print("Table created with success")
    if(insertIntoTable("localhost","root","","devops", "TESTING", "Radoslaw", "1")):
        print("Row added successfully")
    
       
if __name__ == "__main__":
    main()