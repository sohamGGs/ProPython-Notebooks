import sqlite3

def manage_db():
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()

    # Create (Insert)
    cursor.execute("INSERT INTO students (name, branch) VALUES (?, ?)", ("Soham", "CSE"))
    
    # Read (Select)
    cursor.execute("SELECT * FROM students")
    print(f"All Students: {cursor.fetchall()}")

    # Update
    cursor.execute("UPDATE students SET branch = ? WHERE name = ?", ("Data Science", "Soham"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    
    manage_db()