# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:55:58 2019

@author: Radek
"""

import pymysql

def add(x,y):
    return x+y
    
def main():
    #open database connection
    db = pymysql.connect("localhost","root","","company" )
    print("Connected")
      
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print ("Database version : %s " % data)

    # disconnect from server
    db.close()
    
if __name__ == "__main__":
    main()