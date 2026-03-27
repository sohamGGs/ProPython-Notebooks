import sqlite3

def unsafe_way(user_input):
    # DANGEROUS: prone to SQL Injection
    query = f"SELECT * FROM students WHERE name = '{user_input}'"
    return query

def safe_way(user_input):
    # SECURE: Using parameterized queries
    return "SELECT * FROM students WHERE name = ?", (user_input,)

if __name__ == "__main__":
    # Fixed the f-string syntax by avoiding backslashes inside {}
    user_val = "Soham' OR '1'='1"
    print(f"Unsafe Query: {unsafe_way(user_val)}")
    
    query, params = safe_way("Soham")
    print(f"Safe Pattern: {query} | Params: {params}")