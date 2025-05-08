# app/config.py
import sqlite3
import os

DB_PATH = "data/credentials.db"

def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Tabel users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            salt BLOB NOT NULL,
            hashed_password TEXT NOT NULL,
            aes_key BLOB NOT NULL
        )
    ''')
    
    # Tabel kredensial
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            service TEXT,
            username TEXT,
            encrypted_password BLOB,
            PRIMARY KEY (service, username)
        )
    ''')
    
    conn.commit()
    conn.close()