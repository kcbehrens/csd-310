/*
    Title: whatabook_init.sql
    Author: Korbyn Behrens
    Date: Feb 19 2023
    Description: whatabook database initialization script.
*/

-- Drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- Create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- Grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- Drop tables if they are present
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;

-- Drop Constraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- Create all tables needed for the book store
CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

-- Insert user records 
INSERT INTO user(first_name, last_name) 
    VALUES('John', 'Doe');

INSERT INTO user(first_name, last_name, book_id)
    VALUES('Percy', 'Jackson');

INSERT INTO user(first_name, last_name, book_id)
    VALUES('Wade', 'Watts');

-- Insert book records
INSERT INTO book(book_id, book_name, author, details)
    VALUES('1', 'The Lightning Thief', 'Rick Riordan', 'First in the Percy Jackson series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('2', 'The Sea of Monsters', 'Rick Riordan', 'Second in the Percy Jackson series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('3', 'The Titans Curse', 'Rick Riordan', 'Third in the Percy Jackson series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('4', 'The Battle of the Labyrinth', 'Rick Riordan', 'Fourth in the Percy Jackson series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('5', 'The Last Olympian', 'Rick Riordan', 'Fifth in the Percy Jackson series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('6', 'The Lost Hero', 'Rick Riordan', 'First in the Heroes of Olympus series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('7', 'The Son of Neptune', 'Rick Riordan', 'Second in the Heroes of Olympus series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('8', 'The Mark of Athena', 'Rick Riordan', 'Third in the Heroes of Olympus series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('9', 'The House of Hades', 'Rick Riordan', 'Fourth in the Heroes of Olympus series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('10', 'The Blood of Olympus', 'Rick Riordan', 'Fifth in the Heroes of Olympus series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('11', 'Ready Player One', 'Ernest Cline', 'First in the Ready Players One series.');

INSERT INTO book(book_id, book_name, author, details)
    VALUES('12', 'Ready Player Two', 'Ernest Cline', 'Second in the Ready Players One series.');

-- Insert wishlist records
INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'John'), 
        (SELECT book_id FROM book WHERE book_name = 'The Battle of the Labyrinth')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Percy'), 
        (SELECT book_id FROM book WHERE book_name = 'The Blood of Olympus')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Wade'), 
        (SELECT book_id FROM book WHERE book_name = 'Ready Player Two')
    );

-- Insert store record
INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');

INSERT INTO store(locale)
    VALUES('3333 Oak View Dr, Omaha, NE 68144');