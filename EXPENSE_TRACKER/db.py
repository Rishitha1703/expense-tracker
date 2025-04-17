# db.py

import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(amount, category, description):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)',
                   (amount, category, description))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
    conn.commit()
    conn.close()
