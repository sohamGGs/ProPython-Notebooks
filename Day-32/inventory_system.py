import sqlite3

class InventoryDB:
    def __init__(self):
        self.conn = sqlite3.connect("store.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cat (id INT PRIMARY KEY, n TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS prod (id INT PRIMARY KEY, n TEXT, c_id INT)")
    
    def add_data(self):
        self.cur.execute("INSERT OR REPLACE INTO cat VALUES (1, 'Electronics')")
        self.cur.execute("INSERT INTO prod VALUES (101, 'Laptop', 1)")
        self.conn.commit()

    def show_inventory(self):
        self.cur.execute("SELECT prod.n, cat.n FROM prod JOIN cat ON prod.c_id = cat.id")
        return self.cur.fetchall()

if __name__ == "__main__":
    db = InventoryDB()
    db.add_data()
    for p, c in db.show_inventory():
        print(f"Product: {p} | Category: {c}")