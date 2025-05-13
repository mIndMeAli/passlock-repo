# ui/recovery_dialog.py

import tkinter as tk
from tkinter import messagebox
from app import recovery_module
from app import config

class RecoveryDialog(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pemulihan Darurat")
        self.geometry("400x250")
        self.configure(bg="white")
        self.resizable(False, False)

        tk.Label(self, text="Masukkan alamat email pemulihan:", bg="white").pack(pady=(20, 5))
        self.email_entry = tk.Entry(self, width=40)
        self.email_entry.pack(pady=(0, 15))

        tk.Button(self, text="Kirim Email Pemulihan", command=self.send_recovery_email).pack()

    def send_recovery_email(self):
        email = self.email_entry.get().strip()
        if not email:
            messagebox.showerror("Kesalahan", "Alamat email tidak boleh kosong.")
            return

        try:
            recovery_module.send_recovery_email(email)
            messagebox.showinfo("Berhasil", "Email pemulihan telah dikirim.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Gagal", f"Gagal mengirim email.\n\n{str(e)}")