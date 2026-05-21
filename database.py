import sqlite3


def get_db_connection():

    conn = sqlite3.connect("expenses.db")

    return conn


conn = get_db_connection()

cursor = conn.cursor()

# Create categories table
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

# Create expenses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id)
)
""")

conn.commit()
conn.close()

print("Database tables created successfully")