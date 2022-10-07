import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY , username text, password text)"
cursor.execute(create_table)

<<<<<<< HEAD
<<<<<<< HEAD
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
=======
create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
>>>>>>> b1a5cf8 (server/app : add code changes)
=======
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
>>>>>>> a0b222b (server/app : final commit)
cursor.execute(create_table)

connection.commit()

connection.close()


