import sqlite3

def get_student_details():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()
    
    # Inserting sample data
    cursor.execute("INSERT OR IGNORE INTO depts (id, name) VALUES (1, 'CSE'), (2, 'AI-ML')")
    cursor.execute("INSERT INTO students (name, dept_id) VALUES ('Soham', 1), ('Vanshika', 2)")
    
    # The JOIN Query
    query = '''
        SELECT students.name, depts.name 
        FROM students 
        INNER JOIN depts ON students.dept_id = depts.id
    '''
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"Student: {row[0]} | Department: {row[1]}")
    
    conn.close()

if __name__ == "__main__":
    get_student_details()