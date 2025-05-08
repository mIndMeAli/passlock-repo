# app/encryption_module.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_data(data: str, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def decrypt_data(encrypted_data: bytes, key: bytes) -> str:
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size).decode()