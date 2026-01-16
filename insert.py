import sqlite3

conn = sqlite3.connect('nfl_playoffs.db')

cursor = conn.cursor()

query = """
    INSERT INTO points (x,y)
    VALUES
    ('Buffalo', 'Bills'),
    ('New England', 'Patriots'),
    ('Houston', 'Texans'),
    ('Seattle', 'Seahawks'),
    ('San Fransisco', '49ers'),
    ('Chicago', 'Bears'),
    ('Los Angeles', 'Rams')
"""

cursor.execute(query)
conn.commit()
conn.close()

