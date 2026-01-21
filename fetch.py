import sqlite3
import pandas as pd

conn = sqlite3.connect('nfl_playoffs.db')
cursor = conn.cursor()

# Code below selects all the records from the points table
# query = """
#     SELECT * 
#     FROM points;
# """

query = """
    SELECT * 
    FROM points;
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()
# print(records)

# The lines below print out the contents of the database in a dataframe
# records_df = pd.DataFrame(records, columns = ['id', 'city', 'name'])
# print(records_df)

# PRINT OUT LIST OF CITIES
# list_of_city_names = []
# for record in records:
#     list_of_city_names.append(record[1])


# PRINT OUT THE LENGTH OF EACH CITY IN A LIST
# lengths = []
# for record in records:
#     lengths.append(len(record[1]))

# print(lengths)

lengths = []
for record in records:
    lengths.append(len(record[1], record[2]))
print(lengths)