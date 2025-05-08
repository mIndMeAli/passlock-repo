# ui/dialog_windows.py
import tkinter as tk
from tkinter import ttk, messagebox

class AddCredentialDialog(tk.Toplevel):
    def __init__(self, parent, password_manager):
        super().__init__(parent)
        self.pm = password_manager
        self.title("Tambah Kredensial")
        self.geometry("300x200")
        
        ttk.Label(self, text="Layanan:").pack(pady=5)
        self.entry_service = ttk.Entry(self)
        self.entry_service.pack(pady=5)
        
        ttk.Label(self, text="Username:").pack(pady=5)
        self.entry_username = ttk.Entry(self)
        self.entry_username.pack(pady=5)
        
        ttk.Label(self, text="Password:").pack(pady=5)
        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.pack(pady=5)
        
        self.btn_save = ttk.Button(self, text="Simpan", command=self.save)
        self.btn_save.pack(pady=10)

    def save(self):
        service = self.entry_service.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if not service or not username or not password:
            messagebox.showerror("Error", "Semua field harus diisi!")
            return
        
        self.pm.add_credential(service, username, password)
        self.destroy()
        self.master._load_credentials()