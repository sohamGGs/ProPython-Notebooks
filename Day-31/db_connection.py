import sqlite3

# Connect to a database (creates it if it doesn't exist)
conn = sqlite3.connect("student_data.db")
cursor = conn.cursor()

# Create a simple table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        branch TEXT
    )
''')

conn.commit()
conn.close()
print("Database and Table created successfully.")