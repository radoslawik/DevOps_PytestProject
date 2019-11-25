from datab import *

address = "localhost"
user = "root"
password = ""
database = "devops"
table = "TESTING"
    
'''
In putData function connection with database is checked, then couple of operations are proceeded:
 -> table TESTING is created (if table already exists then it is dropped)
 -> three values are inserted into table TESTING
 -> all values in table TESTING are fetched and displayed
'''  
def putData():
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
 -> all values in table TESTING are fetched and displayed
'''  
def getData():
    data = selectFromTable(address,user,password,database,table)
    if(data):
        print("Data fetched successfully")
    return data
    

       
if __name__ == "__main__":
    
    putData()
    data = getData()