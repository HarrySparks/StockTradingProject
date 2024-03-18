import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import subprocess

# Connect to SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table for storing user credentials
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

def register():
    username = username_entry.get()
    password = password_entry.get()

    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        messagebox.showerror("Error", "Username already exists. Please choose another one.")
    else:
        # Insert new user into the database
        c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful.")

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Hash the password to compare with the stored hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username and password match
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    if c.fetchone():
        messagebox.showinfo("Success", "Login successful.")
        subprocess.run(["python", "main.py"])
        root.destroy()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Create main window
root = tk.Tk()
root.title("Login Page")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Register and login buttons
register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Run the main event loop
root.mainloop()

# Close the connection to the database
conn.close()
