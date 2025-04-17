# app.py
import os
import tkinter as tk
from ui import ExpenseApp

if __name__ == "__main__":
    # OpenShift and similar platforms may not have a display
    if os.environ.get("DISPLAY"):
        root = tk.Tk()
        app = ExpenseApp(root)
        root.mainloop()
    else:
        print("No display found. This is a GUI app and cannot run in a server environment.")
