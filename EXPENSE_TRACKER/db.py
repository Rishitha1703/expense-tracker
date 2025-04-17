# db.py
import sqlite3

def connect():
    return sqlite3.connect("expenses.db")

def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT
            )
        """)
        conn.commit()

def add_expense(amount, category, description):
    with connect() as conn:
        conn.execute("INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
                     (amount, category, description))
        conn.commit()

def get_expenses():
    with connect() as conn:
        return conn.execute("SELECT * FROM expenses").fetchall()

def delete_expense(expense_id):
    with connect() as conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()

# Ensure table is created when module is loaded
create_table()
