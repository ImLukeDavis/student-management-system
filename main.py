import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create a table for students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade INTEGER,
        attendance INTEGER,
        course TEXT
    )
''')

# Create a table for courses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
''')

conn.commit()
conn.close()
