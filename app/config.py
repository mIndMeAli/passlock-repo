import os

# Path direktori
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
KEYS_DIR = os.path.join(BASE_DIR, 'keys')

# Pengaturan Email Pemulihan
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@gmail.com"
SMTP_PASSWORD = "your_app_password"  # Gunakan App Password dari Google

# Parameter Keamanan
SALT = b"your_static_salt_here"  # Ganti dengan salt acak di produksi
ITERATIONS = 100000  # Untuk PBKDF2