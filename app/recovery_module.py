import smtplib
from email.mime.text import MIMEText
from app.encryption_module import encrypt_data
from app.config import RECOVERY_EMAIL, RECOVERY_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_recovery_email(recipient_email, recovery_key):
    """
    Kirim email berisi recovery key yang telah dienkripsi.
    """
    try:
        encrypted_key = encrypt_data(recovery_key)

        subject = "PassLock Pro - Recovery Key Anda"
        body = f"""
        Berikut adalah recovery key Anda (harap simpan dengan aman):

        {encrypted_key}

        Jika Anda tidak meminta ini, abaikan email ini.
        """

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = RECOVERY_EMAIL
        msg["To"] = recipient_email

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(RECOVERY_EMAIL, RECOVERY_PASSWORD)
            server.sendmail(RECOVERY_EMAIL, recipient_email, msg.as_string())

        return True

    except Exception as e:
        print(f"[ERROR] Gagal mengirim recovery email: {e}")
        return False
