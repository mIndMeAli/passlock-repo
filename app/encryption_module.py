from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

KEY_FILE = "keys/aes.key"

def generate_key():
    """Generate dan simpan kunci AES 256-bit"""
    key = get_random_bytes(32)  # AES-256
    os.makedirs(os.path.dirname(KEY_FILE), exist_ok=True)
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

def load_key():
    """Muat kunci AES dari file"""
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def pad(s):
    """Pad data agar panjangnya kelipatan 16 (AES block size)"""
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def unpad(s):
    """Hapus padding dari hasil dekripsi"""
    return s[:-ord(s[len(s) - 1:])]

def encrypt(plain_text: str) -> str:
    key = load_key()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text).encode('utf-8'))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return f"{iv}:{ct}"

def decrypt(encrypted_text: str) -> str:
    key = load_key()
    iv, ct = encrypted_text.split(":")
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain = cipher.decrypt(ct).decode('utf-8')
    return unpad(plain)
