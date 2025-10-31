IS211 Assignment 10 – Relational Databases: SQL and SQLite
Overview
This project demonstrates basic database design and interaction using SQLite and Python. It includes:
A music database schema modeled in SQL.
A pets database that’s loaded and queried through Python scripts.
All work is contained in the GitHub repository IS211_Assignment10.

Part I – Music Database (music.sql)
Description
The file music.sql defines three relational tables to model the domain of music:
artist — stores artist names
album — stores albums and links to an artist
song — stores songs, linked to their album
Schema Design
Relationships:
One artist can have many albums.
One album can have many songs.

SQL Structure
CREATE TABLE artist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

CREATE TABLE song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER,
    length_seconds INTEGER,
    FOREIGN KEY (album_id) REFERENCES album(id)
);

Test Example
INSERT INTO artist(name) VALUES ('Nicki Minaj');
INSERT INTO album(name, artist_id) VALUES ('Pink Friday 2', 1);
INSERT INTO song(name, album_id, track_number, length_seconds)
VALUES ('Barbie Dangerous', 1, 1, 201);

Expected output when queried:
Nicki Minaj | Pink Friday 2 | Barbie Dangerous | 1

Part II – Pets Database
Creates a new SQLite database named pets.db
Builds the person, pet, and person_pet tables
Inserts the provided data using executemany()
Prints a confirmation message when complete
Run: python3 load_pets.py
Expected output: Loaded pets.db successfully.

query_pets.py
Run: python3 query_pets.py
Example output: 
Enter person ID (or -1 to exit): 1
James Smith, 41 years old
  James Smith owned Rusty, a Dalmatian, that was 4 years old.
  James Smith owned Bella, an Alaskan Malamute, who is 3 years old.
Enter person ID (or -1 to exit): -1
Exiting. Goodbye!

Purpose of the person_pet Table
The person_pet table models a many-to-many relationship between people and pets.
It links IDs from the person and pet tables, allowing one person to have multiple pets and a pet to belong to multiple people.

How to Verify:
Run sqlite3 pets.db and check:
.tables

Output should include:
person  pet  person_pet

Confirm record counts:
sqlite3 pets.db "SELECT COUNT(*) FROM person;"      # → 4
sqlite3 pets.db "SELECT COUNT(*) FROM pet;"         # → 6
sqlite3 pets.db "SELECT COUNT(*) FROM person_pet;"  # → 6

Files Included
File	Description
music.sql	SQL schema for the music database
load_pets.py	Loads data into pets.db
query_pets.py	Queries the pets database interactively
README.md	Project overview and usage guide
