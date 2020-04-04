# Simple project using DevOps tools & techniques
Calculating distance between two cities using Harvesine formula. Testing simple database queries with PyMySQL and PyTest frameworks. Features of the application consists of:
 - Creating database
 - Testing connection with database
 - Creating a table in database
 - Inserting into table
 - Reading data from table
 - Fetching coordinates of the city from the data
 - Calculating distance between two cities
 - Full unit tests included
 
## Prerequisites
To run this application you need to have installed followed components:
 - [python3](https://www.python.org/downloads/) version 3.8 recommended
 - [mysql](https://dev.mysql.com/) version at least 5.5 (8 recommended)
 - [pytest](https://docs.pytest.org/en/latest/)
 - [pymysql](https://pypi.org/project/PyMySQL/) (only if you want to run application tests)

If you want only to check how this application works you can use [docker](https://www.docker.com/get-started) container. To do so, make sure you have docker installed. You can find the installation guide [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/). After follow the instructions in the __Run in container__ part.

If you have python with pip installed, configuration of libraries is easy. To install them you can just simply type 
```bash
pip install pytest
pip install pymysql
```

## Run application

Clone or download repository. To be able to run the project also make sure that mysql client is running. __WARNING__: Before running the program you can modify the default database name in haversine.py (otherwise existing one with default name will be dropped). Default database name is "pytestproject_testing". 
To run the application just go the project folder and simply use command
```bash
python haversine.py <mysql_address> <mysql_username> <mysql_password>
```
For example:
```bash
python haversine.py localhost root ""
```
__NOTICE__: to set empty value use quotes

To run the tests use instead (also in the project main directory)
```bash
pytest
```
## Run in container

Running the application using docker-compose is very simple. To run the application you can use following command:
```bash
docker-compose --abort-on-container-exit
```
If you are willing to run test you should run:
```bash
docker-compose --file docker-compose-test.yml up --abort-on-container-exit
```

__NOTICE__: if you want to change the default credentials you should modify them in the file docker-compose.yml
