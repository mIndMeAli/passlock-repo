# generate_recovery_key.py
import os
import base64

def generate_recovery_key():
    key = os.urandom(32)  # AES-256
    with open('keys/recovery.key', 'wb') as key_file:
        key_file.write(base64.b64encode(key))
    print("Recovery key generated and saved to keys/recovery.key")

if __name__ == '__main__':
    generate_recovery_key()