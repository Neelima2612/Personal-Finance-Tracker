import sqlite3
import os

def connect_db():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    

    try:
        cursor.execute("SELECT username FROM transactions LIMIT 1")
    except sqlite3.OperationalError:
        print("Re-creating table...")
        cursor.execute("DROP TABLE IF EXISTS transactions")
        

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        username TEXT,
        category TEXT,
        type TEXT,
        amount REAL,
        PRIMARY KEY (username, category)
    )
    """)
    conn.commit()
    conn.close()

def insert_transaction(username, t_type, category, amount):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT OR REPLACE INTO transactions(username, category, type, amount) 
        VALUES (?, ?, ?, ?)
    """, (username, category, t_type, amount))
    
    conn.commit()
    conn.close()

def fetch_transactions(username):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT category, type, amount FROM transactions WHERE username=?", (username,))
    data = cursor.fetchall()
    
    conn.close()
    return data