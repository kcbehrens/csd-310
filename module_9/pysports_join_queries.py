#Title: pysports_join_queries.py
#Author: Korbyn Behrens
#Date: Febuary 6 2023
#Description: pysports inter join players to teams.

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
    
    #Inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    #Results from the query
    players = cursor.fetchall()
    
    #Sleep timer for 2 seconds to gather data for output
    time.sleep(2)
    
    print("\n-- DISPLAYING PLAYER RECORDS --")
    
    #Gather results from players
    for player in players:
        print("\nPlayer ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
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