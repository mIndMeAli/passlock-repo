import tkinter as tk
from tkinter import messagebox
from app.hash_module import hash_master_password

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PassLockPro - Login")
        self.geometry("300x150")

        # Widgets
        self.label = tk.Label(self, text="Masukkan Master Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.authenticate)

        # Layout
        self.label.pack(pady=10)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=10)

    def authenticate(self):
        password = self.password_entry.get()
        hashed_password = hash_master_password(password)
        # Contoh: Bandingkan dengan hash yang tersimpan (belum diimplementasi)
        messagebox.showinfo("Login", "Login Berhasil!" if password else "Gagal!")