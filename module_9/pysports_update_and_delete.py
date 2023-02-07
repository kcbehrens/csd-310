#Title: pysports_update_and_delete.py
#Author: Korbyn Behrens
#Date: Febuary 6 2023
#Description: pysports update player and delete player.

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

def show_players(cursor, title):
    
    #Inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    #Results from the query
    players = cursor.fetchall()
    
    print("\n-- {} --".format(title))
    
    #Gather results from players
    for player in players:
        print("\nPlayer ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

#Shows whether connection is successful or not given the input
try:
    db = mysql.connector.connect(**config)

    #Cursor
    cursor = db.cursor()
    
    #Query to add a new player 
    add_player = ("INSERT INTO player(first_name, last_name, team_id) VALUES(%s, %s, %s)")

    #Player details 
    player_data = ("Cuthulu", "Destroyer of Worlds", 7)

    #Add new player
    cursor.execute(add_player, player_data)

    #Commit to the database
    db.commit()

    #All players (including new)
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #New record 
    update_player = ("UPDATE player SET team_id = 1, first_name = 'Korbyn', last_name = 'Behrens' WHERE first_name = 'Cuthulu'")

    #Query update
    cursor.execute(update_player)

    #Show all records of players
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #Delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Korbyn'")

    cursor.execute(delete_player)

    #All players (after delete) 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")
    
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