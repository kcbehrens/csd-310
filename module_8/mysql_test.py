#Title: mysql_test.py
#Author: Korbyn Behrens
#Date: Jan 31 2023
#Description: pysports database connection test.

#Connects MySQL with Python
import mysql.connector
from mysql.connector import errorcode

#Configuration data for database
config = {
    "host" : "localhost",
    "user" : input("\nUsername: "),
    "password" : input("\nPassword: "),
    "database" : input("\nDatabase: "),
    "raise_on_warnings" : True
    }

#Shows whether connection is successful or not given the input
try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user " + format(config["user"]) + " connected to MySQL on host configuration " + config["host"] + " with database " + config["database"] + ".")
    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\nThe supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\nThe specified database does not exist.")
    else:
        print(err)
        
finally:
    db.close()