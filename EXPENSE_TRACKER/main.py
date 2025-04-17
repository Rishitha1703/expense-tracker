# main.py

import tkinter as tk
import db
from ui import ExpenseApp

if __name__ == "__main__":
    db.init_db()
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()
