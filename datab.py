# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:55:58 2019

@author: Radoslaw Pudelko
"""

# library providing connection to mySQL database
import pymysql

'''
Create database for the data with city coordinates
'''
def createDatabase(address, username, password, database):
    command = "CREATE DATABASE " + database;
    try:
        charSet = "utf8mb4"
        cursorType = pymysql.cursors.DictCursor
        conn = pymysql.connect(host=address, user=username, password=password, charset=charSet, cursorclass=cursorType)
        cursor = conn.cursor()
        check_command = "DROP DATABASE IF EXISTS " + database;
        # execute check command to avoid error
        cursor.execute(check_command)
        cursor.execute(command)
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except:
        print('UNKNOWN ERROR')
        return False
        
    return True
            

'''
Checks connection with database and prints its version
'''
def testConnection(address, username, password, database):
    
    command = "SELECT VERSION()"
    try:
        # open database connection 
        conn = pymysql.connect(address, username, password, database)
        # prepare a cursor object
        cursor = conn.cursor()
        # execute SQL query
        cursor.execute(command)
        # fetch a single row data
        data = cursor.fetchone()
        print("Database version: %s" % data)
        # disconnect from server
        conn.close()
    # error handling
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except:
        return False
        
    return True

'''
Executes CREATE TABLE command to generate new empty table
'''
def createTable(address, username, password, database, table):

    command = "CREATE TABLE " + table + "(CITY VARCHAR(30) NOT NULL, LATITUDE DECIMAL(5,2), LONGITUDE DECIMAL(5,2))"
    try:
        conn = pymysql.connect(address, username, password, database)
        cursor = conn.cursor()
        cursor.execute(command)
        conn.close()
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.ProgrammingError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except:
        print('UNKNOWN ERROR')
        return False
        
    return True
    
'''
Executes SQL INSERT command to add one row to he table
'''
def insertIntoTable(address, username, password, database, table, city, lat, long):

    command = "INSERT INTO " + database + "." + table + "(CITY, LATITUDE, LONGITUDE) VALUES('" + city + "', " + lat + ", " + long +")"
    print(command)
    try:
        conn = pymysql.connect(address, username, password, database)
        cursor = conn.cursor()
        cursor.execute("SET autocommit = 1") # fix for linux
        cursor.execute(command)
        conn.close()
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except pymysql.ProgrammingError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return False
    except:
        print('UNKNOWN ERROR')
        return False
        
    return True

'''
Executes SQL SELECT command to read all data from the table
'''
def selectFromTable(address, username, password, database, table):

    command = "SELECT * FROM " + table
    try:
        conn = pymysql.connect(address, username, password, database)
        cursor = conn.cursor()
        cursor.execute(command)
        # fetch multiple row data
        results = cursor.fetchall()
        for row in results:
            print("{0} {1} {2}".format(row[0], row[1], row[2]))
        conn.close()
    except pymysql.InternalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return None
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return None
    except pymysql.ProgrammingError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return None
    except:
        print('UNKNOWN ERROR')
        return None
        
    return results
    
if __name__ == "__main__":
    createDatabase("localhost", "root", "", "asf")