# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:55:58 2019

@author: Radoslaw Pudelko
"""

# library providing connection to mySQL database
import pymysql

'''
Checks connection with database and prints it's version
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

    command = "CREATE TABLE " + table + "(NAME  VARCHAR(30) NOT NULL, NUMBER INT)"
    try:
        conn = pymysql.connect(address, username, password, database)
        cursor = conn.cursor()
        check_command = "DROP TABLE IF EXISTS " + table;
        # execute check command to avoid error
        cursor.execute(check_command)
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
def insertIntoTable(address, username, password, database, table, name, number):

    command = "INSERT INTO " + table + "(NAME, NUMBER) VALUES('" + name + "', " + number + ")"
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
        print(results)
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
In main function connection with database is checked, then couple of operations are proceeded:
 -> table TESTING is created (if table already exists then it is dropped)
 -> three values are inserted into table TESTING
 -> all values in table TESTING are fetched and displayed
'''  
def main():
    if(testConnection("localhost","root","","devops")):
        print("Connection tested with success")
    if(createTable("localhost","root","","devops", "TESTING")):
        print("Table created with success")
    if(insertIntoTable("localhost","root","","devops", "TESTING", "Radoslaw", "1")):
        print("Row added successfully")
    if(insertIntoTable("localhost","root","","devops", "TESTING", "Joe", "2")):
        print("Row added successfully")
    if(insertIntoTable("localhost","root","","devops", "TESTING", "Sue", "3")):
        print("Row added successfully")
    if(selectFromTable("localhost","root","","devops", "TESTING")):
        print("Data fetched successfully")
    
       
if __name__ == "__main__":
    main()