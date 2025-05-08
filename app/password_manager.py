import json
import os
from app.encryption_module import encrypt_data, decrypt_data

class PasswordManager:
    def __init__(self, aes_key, db_path):
        self.aes_key = aes_key
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            self._init_db()

    def _init_db(self):
        # Buat file baru jika belum ada
        data = []
        encrypted = encrypt_data(json.dumps(data), self.aes_key)
        with open(self.db_path, 'wb') as f:
            f.write(encrypted)

    def _load_data(self):
        with open(self.db_path, 'rb') as f:
            encrypted = f.read()
        decrypted = decrypt_data(encrypted, self.aes_key)
        return json.loads(decrypted)

    def _save_data(self, data):
        encrypted = encrypt_data(json.dumps(data), self.aes_key)
        with open(self.db_path, 'wb') as f:
            f.write(encrypted)

    def add_entry(self, service, username, password):
        data = self._load_data()
        data.append({
            "service": service,
            "username": username,
            "password": password
        })
        self._save_data(data)

    def delete_entry(self, service):
        data = self._load_data()
        data = [entry for entry in data if entry["service"] != service]
        self._save_data(data)

    def get_all_entries(self):
        return self._load_data()