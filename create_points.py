# Create a database and a table
import sqlite3

conn = sqlite3.connect('nfl_playoffs.db') # name of database

cursor = conn.cursor()

# what's actually going in the
query = """ 
CREATE TABLE IF NOT EXISTS points(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x   TEXT,
    y   TEXT
);

"""

cursor.execute(query) # cursor is used to execute the query
conn.commit() # connection commits
conn.close()