import sqlite3
from app.encryption_module import AESCipher
from app.config import DATA_DIR

class PasswordManager:
    def __init__(self, aes_key: bytes):
        self.db_path = os.path.join(DATA_DIR, 'credentials.db')
        self.cipher = AESCipher(aes_key)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY,
                    service TEXT,
                    username TEXT,
                    password TEXT
                )
            ''')

    def add_password(self, service: str, username: str, password: str):
        iv, encrypted_password = self.cipher.encrypt(password)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO passwords (service, username, password)
                VALUES (?, ?, ?)
            ''', (service, username, encrypted_password.hex()))