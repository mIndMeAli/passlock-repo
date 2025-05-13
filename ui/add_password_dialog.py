import tkinter as tk
from tkinter import messagebox
from app.password_manager import add_credential, initialize_db

class AddPasswordDialog:
    def __init__(self, master, master_password):
        self.top = tk.Toplevel(master)
        self.top.title("Tambah Akun")
        self.top.geometry("300x250")

        tk.Label(self.top, text="Nama Layanan:").pack()
        self.service_entry = tk.Entry(self.top)
        self.service_entry.pack()

        tk.Label(self.top, text="Username:").pack()
        self.username_entry = tk.Entry(self.top)
        self.username_entry.pack()

        tk.Label(self.top, text="Password:").pack()
        self.password_entry = tk.Entry(self.top, show="*")
        self.password_entry.pack()

        tk.Button(self.top, text="Simpan", command=lambda: self.save(master_password)).pack(pady=10)

        initialize_db()

    def save(self, master_password):
        service = self.service_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not service or not username or not password:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi.")
            return

        add_credential(service, username, password, master_password)
        messagebox.showinfo("Sukses", "Data akun berhasil disimpan.")
        self.top.destroy()