import psycopg2


# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database, same as a set/list (array in JS)
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "ARTIST"')

# fetch the results (multiple records from database)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# once results have been fetched, close the connection to the database
connection.close()

# print results
for result in results:
    print(result)
