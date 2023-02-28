#Title: whatabook_behrens.py
#Author: Korbyn Behrens
#Date: Feb 24 2023
#Description: Whatabook store active code.

#Connects MySQL with Python and imports
import sys
import mysql.connector
from mysql.connector import errorcode

#Configuration data for database
config = {
    "host" : "localhost",
    "user" : input("Username: "), #Use whatabook_user
    "password" : input("Password: "), #Use MySQL8IsGreat!
    "database" : input("Database: "), #Use whatabook
    "raise_on_warnings" : True
    }

#Main menu for the program
def show_menu():
    print("\n--Main Menu--")

    print("\n1.View Books\n2.View Store Locations\n3.My Account\n4.Exit Program")

    try:
        choice = int(input("\nPlease select a number 1-4: "))

        return choice
    except ValueError:
        print("\nInvalid character, program terminated...\n")

        sys.exit(0)

#Show books from store
def show_books(_cursor):
    #Inner join query
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    #Get the results from the cursor object
    books = _cursor.fetchall()

    print("\n--WHATABOOK BOOK LISTING--\n")
    
    #Lists book results in designated order 
    for book in books:
        print("\nBook ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2], book[3]))

#Show store locations
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n--WHATABOOK STORE LOCATIONS--")

    for location in locations:
        print("\nLocal Store: {}\n".format(location[1]))

#Validate that user id is good
def validate_user():
    try:
        user_id = int(input("\nWhat is your user id? "))

        if user_id < 0 or user_id > 3:
            print("\nInvalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    
    except ValueError:
        print("\nInvalid number, program terminated...\n")
        sys.exit(0)

#Show the menu when selecting account
def show_account_menu():

    try:
        print("\n--Customer Menu--")
        print("\n1. Wishlist\n2. Add Book To Wishlist\n3. Delete Book From Wishlist\n4. Main Menu")
        account_option = int(input("\nPlease choose a number 1-4: "))

        return account_option
    except ValueError:
        print("\nInvalid number, program terminated...\n")
        sys.exit(0)

#Show what is in the wishlist of the user
def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n--WHATABOOK WISHLIST ITEMS--")

    for book in wishlist:
        print("\nBook ID: {}\nBook Name: {}\nAuthor: {}\n".format(book[3], book[4], book[5]))

#Shows all the books not on the current user's wishlist
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n--WHATABOOK AVAILABLE BOOKS--")

    for book in books_to_add:
        print("\nBook Id: {}\nBook Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#Try/catch block for handling potential MySQL database errors
try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user " + format(config["user"]) + " connected to MySQL on host configuration " + config["host"] + " with database " + config["database"] + ".")
    
    #Cursor for MySQL queries
    cursor = db.cursor()

    print("\nWelcome to the WhatABook Store!")
    
    #Show the main menu
    user_selection = show_menu()
    
    #When the user does not select the option 4
    while user_selection != 4:

        #If the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        #If the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        #If the user selects option 3, call the validate_user method to validate the entered user_id and call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            #While account option does is not 4
            while account_option != 4:

                #If the use selects option 1, call the show_wishlist() method to show the current users configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                #If the user selects option 2, call the show_books_to_add function
                if account_option == 2:

                    #Show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    #Get the entered book_id 
                    book_id = int(input("\nEnter the id of the book you want to add to your wishlist: "))
                    
                    #Add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    
                    #Commit the changes to the database
                    db.commit()

                    print("\nBook id: {} was added to your wishlist!".format(book_id))
                
                '''#If the user selects option 3, call the show_wishlist function
                if account_option == 3:

                    #Show the books currently configured in the users wishlist
                    show_wishlist(cursor, my_user_id)

                    #Get the entered book for removal 
                    bookRemoval = int(input("\nEnter the id of the book you want to delete from your wishlist: "))
                    
                    #Remove item function
                    removeItem = "DELETE FROM show_wishlist WHERE itemName = %s"
                    
                    #Add the selected book the users wishlist
                    cursor.execute(removeItem, (bookRemoval))
                    
                    #Commit the changes to the database
                    db.commit()

                    print("\nBook id: {} was deleted from your wishlist.".format(book_id))
                    
                    #Trying to find a way to delete from the wishlist if a user wanted to. Is a work in progress.'''

                #If the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please retry...")

                #Show the account menu 
                account_option = show_account_menu()
        
        #If the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please retry...")
            
        #Show the main menu
        user_selection = show_menu()

    print("\nProgram terminated...")

#Error out for login to the database
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    db.close()