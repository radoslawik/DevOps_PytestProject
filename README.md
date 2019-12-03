# DevOps_PytestProject
Calculating distance between two cities using Harvesine formula. Testing simple database queries with Pytest framework. Features of the application consists of:
 - Creating database
 - Testing connection with database
 - Creating a table in database
 - Inserting into table
 - Reading data from table
 - Fetching coordinates of the city from the data
 - Calculating distance between two cities
 
# Prerequisites
To run this application you need to have installed followed components:
 - [python3](https://www.python.org/downloads/) version 3.8 recommended
 - [mysql](https://dev.mysql.com/) version at least 5.5 (8 recommended)
 - [pytest](https://docs.pytest.org/en/latest/)
 - [pymysql](https://pypi.org/project/PyMySQL/)

If you have python with pip installed, configuration of libraries is easy. To install them you can just simply type 
```bash
pip install pytest
pip install pymysql
```

# Running application

Clone or download repository. To be able to run the project also make sure that mysql client is running. WARNING: Before running the program you can modify the default database name in haversine.py (otherwise existing one with default name will be dropped). Default database name is "pytestproject_testing". 
To run the application just go the project folder and simply use command
```bash
python haversine.py <mysql_address> <mysql_username> <mysql_password>
```
For example:
```bash
python haversine.py localhost root ""
```
NOTICE: to set empty value use quotes

To run the tests use instead (also in the project main directory)
```bash
pytest
```
NOTICE: mySQL server address, username and password have to be changes in test_haversine.py and test_datab.py

sudo docker-compose --file docker-compose-test.yml up --abort-on-container-exit

# Student info
PUDELKO Radoslaw