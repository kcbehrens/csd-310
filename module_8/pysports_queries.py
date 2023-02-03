#Title: pysports_queries.py
#Author: Korbyn Behrens
#Date: Febuary 2 2023
#Description: pysports database display script.

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
    #Selecting the query
    SELECT team_id, team_name, mascot FROM team;

    #Cursor
    cursor = db.cursor()
    cursor.execute(“SELECT team_id, team_name, mascot FROM team”)
    teams = cursor.fetchall()

    for team in teams:
        print("Team Name: {}".format(team[1]))
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