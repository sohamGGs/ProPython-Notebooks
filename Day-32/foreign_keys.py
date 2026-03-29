import sqlite3

def setup_relational_db():
    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()
    
    # Parent Table
    cursor.execute("CREATE TABLE IF NOT EXISTS depts (id INTEGER PRIMARY KEY, name TEXT)")
    
    # Child Table with Foreign Key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            dept_id INTEGER,
            FOREIGN KEY(dept_id) REFERENCES depts(id)
        )
    ''')
    conn.commit()
    conn.close()

setup_relational_db()
