from datab import *
from math import radians, cos, sin, asin, sqrt
import sys

address = []
password = []
user = []
table = []
database = []
'''
In putData function connection with database is checked, then couple of operations are proceeded:
 -> database is created (if database already exists then it is dropped)
 -> table test_table is created
 -> three values are inserted into table
'''  
def putData(address, user, password, database, table):
    if(createDatabase(address,user,password,database)):
        print("Database now exists")
    else:
        return False
    if(testConnection(address,user,password,database)):
        print("Connection tested with success")
    else:
        return False
    if(createTable(address,user,password,database,table)):
        print("Table created with success")
    else:
        return False
    if(insertIntoTable(address,user,password,database,table, "Paris", "48.85", "2.35")):
        print("Row added successfully")
    else:
        return False
    if(insertIntoTable(address,user,password,database,table, "Rome", "41.89", "12.51")):
        print("Row added successfully")
    else:
        return False
    if(insertIntoTable(address,user,password,database,table, "Cracow", "50.04", "19.94")):
        print("Row added successfully")
    else:
        return False
    return True
    
'''
In getData function:
 -> all values in table are fetched and displayed
'''  
def getData(address, user, password, database, table):
    data = selectFromTable(address,user,password,database,table)
    if(data):
        print("Data fetched successfully")
    return data

"""
Get the city coordinates
"""  
def getCords(results, city):
    if(results == None):
        print("No data provided")
        return None
    if(city == ""):
        print("No city specified")
        return None
    for row in results:
        if(row[0] == city):
            return (row[1], row[2]) # latitude and longitude
    print("Couldn't find this city")
    return None
            
"""
Calculate the distance between two cities using haversine formula
"""
def calcDistance(city1, city2):
    
    # convert coordinates to float
    lat1 = float(city1[0])
    lon1 = float(city1[1])
    lat2 = float(city2[0])
    lon2 = float(city2[1])
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6370 # earth radius
    ans = str(round(c*r, 2)) # round and save as string to simplify
    return ans

def main(address, user, password, database, table):

    putData(address, user, password, database, table) # put data into database -> values specified in datab.py
    data = getData(address, user, password, database, table) # retrieve data from database
    cordCracow = getCords(data, "Cracow") #retrieve city coordinates
    cordParis = getCords(data, "Paris")
    cordRome = getCords(data, "Rome")
    
    print("Distance between Paris and Rome [km]: " )
    print(calcDistance(cordParis, cordRome)) # calculate and print result
    
    print("Distance between Cracow and Rome [km]: " )
    print(calcDistance(cordCracow, cordRome))
    
    print("Distance between Paris and Cracow [km]: " )
    print(calcDistance(cordParis, cordCracow))   
     
if __name__ == "__main__":

    database = "pytestproject_testing" #WARNING: existing database with that name will be dropped
    table = "test_table"
    if(len(sys.argv) != 4):
        print("Wrong arguments! Trying with default ones")
        address = "localhost"
        user = "root"
        password = ""
    else:
        address = sys.argv[1]
        user = sys.argv[2]
        password = sys.argv[3]
    main(address, user, password, database, table)
 