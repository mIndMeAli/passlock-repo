# app/password_manager.py
import sqlite3
from app.config import DB_PATH
from app.encryption_module import encrypt_data, decrypt_data

class PasswordManager:
    def __init__(self, username):
        self.username = username
        self.aes_key = self._get_aes_key()
    
    def _get_aes_key(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT aes_key FROM users WHERE username = ?', (self.username,))
        aes_key = cursor.fetchone()[0]
        conn.close()
        return aes_key
    
    def add_credential(self, service, username, password):
        encrypted_password = encrypt_data(password, self.aes_key)
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO credentials (service, username, encrypted_password)
            VALUES (?, ?, ?)
        ''', (service, username, encrypted_password))
        conn.commit()
        conn.close()
    
    def get_credentials(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT service, username, encrypted_password FROM credentials')
        credentials = [
            (service, username, decrypt_data(encrypted_password, self.aes_key))
            for service, username, encrypted_password in cursor.fetchall()
        ]
        conn.close()
        return credentials