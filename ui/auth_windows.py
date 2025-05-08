import tkinter as tk
from ui.main_window import DashboardWindow 
from tkinter import ttk, messagebox
from app.hash_module import generate_salt, hash_password
from app.config import init_db
import sqlite3

class AuthWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        init_db()
        self.title("PassLock Pro - Login")
        self.geometry("400x300")
        self._setup_ui()

    def _setup_ui(self):
        self.lbl_title = ttk.Label(self, text="Login", font=('Helvetica', 16))
        self.entry_username = ttk.Entry(self, width=30)
        self.entry_password = ttk.Entry(self, width=30, show="*")
        self.btn_login = ttk.Button(self, text="Login", command=self.attempt_login)
        self.btn_signup = ttk.Button(self, text="Daftar", command=self.open_signup)

        self.lbl_title.pack(pady=20)
        ttk.Label(self, text="Username:").pack()
        self.entry_username.pack(pady=5)
        ttk.Label(self, text="Password:").pack()
        self.entry_password.pack(pady=5)
        self.btn_login.pack(pady=10)
        self.btn_signup.pack(pady=5)

    def attempt_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        conn = sqlite3.connect("data/credentials.db")
        cursor = conn.cursor()
        cursor.execute('SELECT salt, hashed_password FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        conn.close()

        if not result:
            messagebox.showerror("Error", "User tidak ditemukan!")
            return

        salt, stored_hash = result
        entered_hash = hash_password(password, salt)

        if entered_hash == stored_hash:
            self.withdraw()
            DashboardWindow(self, username)
        else:
            messagebox.showerror("Error", "Password salah!")

    def open_signup(self):
        SignupWindow(self)

class SignupWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("PassLock Pro - Daftar")
        self.geometry("400x350")
        self.salt = None
        self._setup_ui()

    def _setup_ui(self):
        self.lbl_title = ttk.Label(self, text="Buat Akun Baru", font=('Helvetica', 14))
        self.entry_username = ttk.Entry(self, width=25)
        self.entry_password = ttk.Entry(self, width=25, show="*")
        self.btn_generate_salt = ttk.Button(self, text="Generate Salt", command=self._generate_salt)
        self.lbl_salt = ttk.Label(self, text="Salt: Belum dibuat", foreground="gray")
        self.btn_signup = ttk.Button(self, text="Daftar", command=self.process_signup)
        self.btn_back = ttk.Button(self, text="Kembali", command=self.destroy)

        self.lbl_title.pack(pady=10)
        ttk.Label(self, text="Username:").pack()
        self.entry_username.pack(pady=5)
        ttk.Label(self, text="Password:").pack()
        self.entry_password.pack(pady=5)
        self.btn_generate_salt.pack(pady=5)
        self.lbl_salt.pack(pady=2)
        self.btn_signup.pack(pady=15)
        self.btn_back.pack(pady=5)

    def _generate_salt(self):
        self.salt = generate_salt()
        self.lbl_salt.config(text=f"Salt: {self.salt.hex()[:8]}...", foreground="green")

    def process_signup(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password wajib diisi!")
            return

        if not self.salt:
            messagebox.showerror("Error", "Generate salt terlebih dahulu!")
            return

        aes_key = hash_password(password, self.salt)[:16]

        conn = sqlite3.connect("data/credentials.db")
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (username, salt, hashed_password, aes_key)
                VALUES (?, ?, ?, ?)
            ''', (username, self.salt, hash_password(password, self.salt), aes_key))
            conn.commit()
            messagebox.showinfo("Sukses", "Akun berhasil dibuat!")
            self.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username sudah ada!")
        finally:
            conn.close()