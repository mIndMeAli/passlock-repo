from Crypto.Protocol.KDF import PBKDF2
from app.config import SALT, ITERATIONS

def hash_master_password(password: str) -> bytes:
    """Hash master password menggunakan PBKDF2 + SHA-256."""
    return PBKDF2(password, SALT, dkLen=32, count=ITERATIONS, hmac_hash_module=SHA256)