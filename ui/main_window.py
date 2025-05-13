import tkinter as tk
from tkinter import messagebox
from app.hash_module import verify_master_password
from ui.biometric_screen import BiometricScreen
from ui.add_password_dialog import AddPasswordDialog

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("PassLock Pro - Login")
        self.root.geometry("400x280")
        self.root.resizable(False, False)

        self.setup_login_ui()

    def setup_login_ui(self):
        self.clear_widgets()

        self.label = tk.Label(self.root, text="Masukkan Master Password", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.verify_login)
        self.login_button.pack(pady=10)

        self.recovery_button = tk.Button(self.root, text="Recovery", command=self.recovery_password)
        self.recovery_button.pack(pady=5)

    def verify_login(self):
        password = self.password_entry.get()
        if verify_master_password(password):
            self.master_password = password
            self.open_dashboard()
        else:
            messagebox.showerror("Login Gagal", "Master password salah!")

    def open_dashboard(self):
        self.clear_widgets()
        self.root.title("PassLock Pro - Dashboard")

        welcome_label = tk.Label(self.root, text="Selamat Datang di PassLock Pro", font=("Helvetica", 14))
        welcome_label.pack(pady=20)

        biometric_button = tk.Button(self.root, text="Buka Simulasi Biometrik", command=self.open_biometric)
        biometric_button.pack(pady=10)
        
        add_button = tk.Button(self.root, text="Tambah Password", command=self.open_add_password_dialog)
        add_button.pack(pady=10)

        view_button = tk.Button(self.root, text="Lihat Akun Tersimpan", command=self.show_stored_accounts)
        view_button.pack(pady=10)

    def show_stored_accounts(self):
        from app.password_manager import get_all_accounts
        accounts = get_all_accounts(self.master_password)

        if not accounts:
            messagebox.showinfo("Data Kosong", "Belum ada akun yang tersimpan.")
            return

        top = tk.Toplevel(self.root)
        top.title("Akun Tersimpan")

        for service, username, password in accounts:
            tk.Label(top, text=f"Layanan: {service}").pack(anchor='w')
            tk.Label(top, text=f"Username: {username}").pack(anchor='w')
            tk.Label(top, text=f"Password: {password}").pack(anchor='w')
            tk.Label(top, text="-"*40).pack()

    def open_biometric(self):
        BiometricScreen(self.root, self.biometric_success)
    
    def biometric_success(self):
        messagebox.showinfo("Berhasil", "Autentikasi biometrik berhasil.")

    def open_add_password_dialog(self):
        AddPasswordDialog(self.root, self.master_password)

    def recovery_password(self):
        messagebox.showinfo("Recovery", "Fitur recovery masih dalam pengembangan.")

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()