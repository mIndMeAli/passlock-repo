import os

# Direktori dasar
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path penyimpanan
KEY_DIR = os.path.join(BASE_DIR, 'keys')
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# Email recovery
RECOVERY_EMAIL = "passlockpro.noreply@gmail.com"
EMAIL_PASSWORD = "abcdefghijklmnop"  # App Password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Parameter enkripsi
AES_KEY_SIZE = 32  # 256-bit AES
BLOCK_SIZE = 16    # AES block size
HASH_ITERATIONS = 100_000  # Untuk derivasi kunci

# Nama file
MASTER_KEY_FILE = os.path.join(KEY_DIR, 'master.key')
RECOVERY_KEY_FILE = os.path.join(KEY_DIR, 'recovery.key')
DB_FILE = os.path.join(DATA_DIR, 'credentials.db')
LOG_FILE = os.path.join(LOG_DIR, 'access_log.txt')