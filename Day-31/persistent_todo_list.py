import sqlite3

class TodoDB:
    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")
        self.conn.commit()

    def add_task(self, task_name):
        self.cur.execute("INSERT INTO tasks (task) VALUES (?)", (task_name,))
        self.conn.commit()

    def show_tasks(self):
        self.cur.execute("SELECT * FROM tasks")
        return self.cur.fetchall()

if __name__ == "__main__":
    app = TodoDB()
    app.add_task("Finish Python Day 31")
    tasks = app.show_tasks()
    for t in tasks:
        print(f"ID: {t[0]} | Task: {t[1]}")
        