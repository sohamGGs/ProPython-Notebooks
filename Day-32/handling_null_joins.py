import sqlite3

def left_join_example():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()
    
    # Student with no department (dept_id is NULL)
    cursor.execute("INSERT INTO students (name, dept_id) VALUES ('New Student', NULL)")
    
    cursor.execute('''
        SELECT students.name, depts.name 
        FROM students 
        LEFT JOIN depts ON students.dept_id = depts.id
    ''')
    
    for row in cursor.fetchall():
        dept = row[1] if row[1] else "Unassigned"
        print(f"Name: {row[0]:<12} | Dept: {dept}")
    
    conn.close()

left_join_example()