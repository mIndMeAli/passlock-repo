#app/password_manager.py
import sqlite3
import os
from app.encryption_module import encrypt_data, decrypt_data, get_aes_key

DB_PATH = "data/credentials.db"

def initialize_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT,
                username TEXT,
                password TEXT
            )
        """)
        conn.commit()

def add_credential(service: str, username: str, password: str, master_password: str):
    key = get_aes_key(master_password)
    encrypted_username = encrypt_data(username, key)
    encrypted_password = encrypt_data(password, key)
    encrypted_service = encrypt_data(service, key)  # Kalau mau service juga dienkripsi

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO credentials (service, username, password) VALUES (?, ?, ?)",
                       (encrypted_service, encrypted_username, encrypted_password))
        conn.commit()
def get_all_accounts(master_password: str):
    """Mengambil dan mendekripsi semua akun dari database"""
    key = get_aes_key(master_password)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS credentials (id INTEGER PRIMARY KEY AUTOINCREMENT, service TEXT, username TEXT, password TEXT)")
    cursor.execute("SELECT service, username, password FROM credentials")
    rows = cursor.fetchall()
    conn.close()

    decrypted_accounts = []
    for encrypted_service, encrypted_username, encrypted_password in rows:
        try:
            service = decrypt_data(encrypted_service, key)
            username = decrypt_data(encrypted_username, key)
            password = decrypt_data(encrypted_password, key)
            decrypted_accounts.append((service, username, encrypted_password))
            
        except Exception as e:
            print(f"Error decrypting account for {service}: {e}")

    return decrypted_accounts