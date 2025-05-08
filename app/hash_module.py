# app/hash_module.py
import os
from Crypto.Hash import SHA256

def generate_salt():
    return os.urandom(16)

def hash_password(password: str, salt: bytes) -> bytes:
    sha = SHA256.new()
    sha.update(password.encode() + salt)
    return sha.digest()