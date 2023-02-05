#Title: pysports_queries.py
#Author: Korbyn Behrens
#Date: Febuary 2 2023
#Description: pysports database display script.

#Connects MySQL with Python
import mysql.connector
from mysql.connector import errorcode
import time

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

    #Cursor
    cursor = db.cursor()
    
    #Select the query
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    
    #Sleep timer for 2 seconds to gather data for output
    time.sleep(2)
    
    #Results from the query
    teams = cursor.fetchall()
    print("-- DISPLAYING TEAM RECORDS --")
    
    #Gather results from teams
    for team in teams:
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))
    
    #Select player table information
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    
    #Results from the query
    players = cursor.fetchall()
    print ("\n-- DISPLAYING PLAYER RECORDS --")

    #Gather the results of the players
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\nPress any key to continue... ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\nThe supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\nThe specified database does not exist.")
    else:
        print(err)
    
finally:
    db.close()