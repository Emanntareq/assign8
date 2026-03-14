import sqlite3

# Connect to the database (ensure quiz.db is in the same directory or specify full path)
conn = sqlite3.connect('quiz.db')

# Create a cursor object
cursor = conn.cursor()

# Fetch data from the sessions table
cursor.execute("SELECT * FROM sessions")

# Print the results
print(cursor.fetchall())

# Close the connection
conn.close()
