import hashlib
import os

HASH_FILE = "keys/master.key"

def hash_password(password: str) -> str:
    """Mengubah password menjadi hash SHA-256."""
    sha = hashlib.sha256()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()

def save_hashed_password(password: str):
    """Menyimpan hash password ke file master.key"""
    hashed = hash_password(password)
    os.makedirs(os.path.dirname(HASH_FILE), exist_ok=True)
    with open(HASH_FILE, 'w') as f:
        f.write(hashed)

def verify_password(input_password: str) -> bool:
    """Memverifikasi password pengguna dengan hash tersimpan"""
    if not os.path.exists(HASH_FILE):
        return False  # belum ada password tersimpan

    with open(HASH_FILE, 'r') as f:
        saved_hash = f.read().strip()

    return hash_password(input_password) == saved_hash
