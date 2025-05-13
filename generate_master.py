import hashlib

password = "gemboks123"  # Ganti dengan password yang kamu inginkan
hashed = hashlib.sha256(password.encode()).hexdigest()

with open("keys/master.key", "w") as f:
    f.write(hashed)

print("Master password hash disimpan.")