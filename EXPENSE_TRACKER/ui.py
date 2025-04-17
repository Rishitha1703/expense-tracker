# ui.py

import tkinter as tk
from tkinter import ttk, messagebox
import db

class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Center the window
        window_width = 800
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        root.resizable(False, False)

        # Set colorful background
        root.configure(bg="#f0f4ff")  # soft blue background

        # Frame for form
        form_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, bd=2, relief=tk.GROOVE)
        form_frame.place(x=50, y=50, width=300, height=220)

        tk.Label(form_frame, text="Amount", bg="#ffffff", fg="#333", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
        self.amount_entry = tk.Entry(form_frame)
        self.amount_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Category", bg="#ffffff", fg="#333", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")
        self.category_entry = tk.Entry(form_frame)
        self.category_entry.grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="Description", bg="#ffffff", fg="#333", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w")
        self.description_entry = tk.Entry(form_frame)
        self.description_entry.grid(row=2, column=1, pady=5)

        add_btn = tk.Button(form_frame, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        add_btn.grid(row=3, columnspan=2, pady=10)

        # Table frame
        table_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
        table_frame.place(x=380, y=50, width=380, height=400)

        self.tree = ttk.Treeview(table_frame, columns=("ID", "Amount", "Category", "Description"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90)
        self.tree.pack(fill="both", expand=True)

        # Delete button
        del_btn = tk.Button(root, text="Delete Selected", command=self.delete_expense,
                            bg="#f44336", fg="white", font=("Arial", 10, "bold"))
        del_btn.place(x=540, y=470, width=150, height=30)

        self.load_expenses()

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            description = self.description_entry.get()
            db.add_expense(amount, category, description)
            self.load_expenses()
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid input", "Amount must be a number")

    def load_expenses(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in db.get_expenses():
            self.tree.insert("", "end", values=row)

    def delete_expense(self):
        selected = self.tree.selection()
        if selected:
            expense_id = self.tree.item(selected[0])["values"][0]
            db.delete_expense(expense_id)
            self.load_expenses()
        else:
            messagebox.showwarning("No selection", "Please select a row to delete")
