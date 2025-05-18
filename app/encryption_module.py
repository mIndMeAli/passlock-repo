#app/encryption_module.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64
import os

BLOCK_SIZE = 16  # AES block size

def get_aes_key(master_password: str) -> bytes:
    """Menghasilkan kunci AES dari hash SHA-256 master password"""
    return hashlib.sha256(master_password.encode()).digest()  # 32 bytes

def encrypt_data(plain_text: str, key: bytes) -> str:
    """Mengenkripsi teks dengan AES dan mengembalikan base64 string"""
    iv = os.urandom(BLOCK_SIZE)  # IV harus random tiap enkripsi
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(plain_text.encode(), BLOCK_SIZE))
    return base64.b64encode(iv + encrypted).decode()

def decrypt_data(encrypted_base64: str, key: bytes) -> str:
    """Mendekripsi base64 string menggunakan AES dan kunci"""
    raw = base64.b64decode(encrypted_base64)
    iv = raw[:BLOCK_SIZE]
    encrypted = raw[BLOCK_SIZE:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), BLOCK_SIZE)
    return decrypted.decode()