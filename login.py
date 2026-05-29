import tkinter as tk
from tkinter import messagebox
import sqlite3

# =========================
# DATABASE INITIALIZATION
# =========================
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# =========================
# REGISTER FUNCTION
# =========================
def register():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "Username and Password cannot be empty!")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            messagebox.showerror("Registration Failed", "Username already exists! Try another one.")
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully! Now click Login.")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")
    finally:
        conn.close()

# =========================
# LOGIN FUNCTION
# =========================
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    data = cursor.fetchone()
    conn.close()

    if data:
        messagebox.showinfo(
            "Login Success",
            "Welcome to Finance Tracker!"
        )
        window.destroy()
        
        try:
            import main  
            main.start_app(username)  
        except ImportError:
            messagebox.showerror("Error", "main.py file not found!")
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password"
        )

# =========================
# MAIN WINDOW
# =========================
window = tk.Tk()
window.title("Finance Tracker Login & Register")
window.geometry("450x550") 
window.config(bg="#1b2436")
window.resizable(False, False)

# =========================
# TITLE
# =========================
title = tk.Label(
    window,
    text="LOGIN SYSTEM",
    font=("Times New Roman", 28, "bold"),
    bg="#1b2436",
    fg="white"
)
title.pack(pady=30)

# =========================
# USERNAME WIDGETS
# =========================
username_label = tk.Label(
    window,
    text="Username",
    font=("Arial", 14, "bold"),
    bg="#1b2436",
    fg="white"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=25,
    bd=5
)
username_entry.pack(pady=5)

# =========================
# PASSWORD WIDGETS
# =========================
password_label = tk.Label(
    window,
    text="Password",
    font=("Arial", 14, "bold"),
    bg="#1b2436",
    fg="white"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=25,
    bd=5,
    show="*"
)
password_entry.pack(pady=5)

# =========================
# ACTION BUTTONS CONTAINER
# =========================
btn_frame = tk.Frame(window, bg="#1b2436")
btn_frame.pack(pady=25)

# LOGIN BUTTON
login_btn = tk.Button(
    btn_frame,
    text="Login",
    font=("Arial", 14, "bold"),
    bg="#6a4bc4",
    fg="white",
    width=18,
    pady=6,
    cursor="hand2",
    command=login
)
login_btn.pack(pady=10)

# NEW REGISTER BUTTON
register_btn = tk.Button(
    btn_frame,
    text="Register / Sign Up ",
    font=("Arial", 12, "bold"),
    bg="#23c483", 
    fg="white",
    width=20,
    pady=6,
    cursor="hand2",
    command=register
)
register_btn.pack(pady=5)

window.mainloop()