import sqlite3

# Connect to database
connection = sqlite3.connect("questions.db")

# Create cursor
cursor = connection.cursor()

# Create leaderboard table
cursor.execute("""

CREATE TABLE IF NOT EXISTS leaderboard (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT NOT NULL,

    score INTEGER NOT NULL

)

""")

print("Database created successfully!")

# Save changes
connection.commit()

# Close connection
connection.close()