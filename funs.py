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
        return e.args[0]
    except pymysql.OperationalError as e:
        print('ERROR: {!r}, errno is {}'.format(e, e.args[0]))
        return e.args[0]
    
    return 0
    
def main():
    if(testConnection("localhost","root","","devops") == 0):
        print("Connection tested with success") 
    
if __name__ == "__main__":
    main()