import os
import random
import tkinter as tk
from tkinter import messagebox, ttk
from twilio.rest import Client

from app.hash_module import verify_master_password, hash_password
from app.encryption_module import get_aes_key, decrypt_data
from app.password_manager import get_all_accounts
from ui.biometric_screen import BiometricScreen
from ui.add_password_dialog import AddPasswordDialog

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.master_password = None
        self._configure_window()
        self._setup_login_ui()

    def _configure_window(self):
        """Konfigurasi dasar window"""
        self.root.title("PassLock Pro - Login")
        self.root.geometry("400x280")
        self.root.resizable(False, False)

    def _setup_login_ui(self):
        """Membuat antarmuka login"""
        self.clear_widgets()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        ttk.Label(main_frame, 
                text="Masukkan Master Password", 
                font=("Helvetica", 14)).pack(pady=10)

        self.password_entry = ttk.Entry(main_frame, show="•", width=30)
        self.password_entry.pack(pady=5)

        ttk.Button(main_frame, 
                text="Login", 
                command=self.verify_login).pack(pady=10)

        ttk.Button(main_frame,
                text="Recovery",
                command=self.recovery_password).pack(pady=5)

    def verify_login(self):
        """Verifikasi master password"""
        password = self.password_entry.get()
        if verify_master_password(password):
            self.master_password = password
            self._open_dashboard()
        else:
            messagebox.showerror("Login Gagal", "Master password salah!")

    def _open_dashboard(self):
        """Membuka dashboard utama"""
        self.clear_widgets()
        self.root.title("PassLock Pro - Dashboard")

        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        ttk.Label(main_frame, 
                text="Selamat Datang di PassLock Pro", 
                font=("Helvetica", 14)).pack(pady=10)

        ttk.Button(main_frame,
                text="Buka Simulasi Biometrik",
                command=self.open_biometric).pack(pady=5)

        ttk.Button(main_frame,
                text="Tambah Password",
                command=self.open_add_password_dialog).pack(pady=5)

        ttk.Button(main_frame,
                text="Lihat Akun Tersimpan",
                command=self.show_stored_accounts).pack(pady=5)

    def show_stored_accounts(self):
        """Menampilkan akun tersimpan"""
        accounts = get_all_accounts(self.master_password)

        if not accounts:
            messagebox.showinfo("Data Kosong", "Belum ada akun yang tersimpan.")
            return

        window = tk.Toplevel(self.root)
        window.title("Akun Tersimpan")
        
        main_frame = ttk.Frame(window)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Header
        headers = ["Layanan", "Username", "Password"]
        for col, header in enumerate(headers):
            ttk.Label(main_frame, 
                    text=header, 
                    font=('Helvetica', 10, 'bold'),
                    background='#e0e0e0').grid(
                        row=0, 
                        column=col, 
                        padx=5, 
                        pady=5, 
                        sticky='ew'
                    )

        # Konten
        for row, (service, username, encrypted_password) in enumerate(accounts, start=1):
            bg_color = '#f0f0f0' if row % 2 == 0 else 'white'
            
            ttk.Label(main_frame, 
                    text=service, 
                    background=bg_color).grid(
                        row=row, 
                        column=0, 
                        padx=5, 
                        pady=2, 
                        sticky='w'
                    )
            
            ttk.Label(main_frame, 
                    text=username, 
                    background=bg_color).grid(
                        row=row, 
                        column=1, 
                        padx=5, 
                        pady=2, 
                        sticky='w'
                    )

            self._create_password_widget(main_frame, row, encrypted_password, bg_color)

        # Konfigurasi grid
        for col in range(3):
            main_frame.grid_columnconfigure(col, weight=1)

    def _create_password_widget(self, parent, row, encrypted_password, bg_color):
        """Membuat widget password dengan toggle"""
        frame = ttk.Frame(parent)
        frame.grid(row=row, column=2, padx=5, pady=2, sticky='w')

        entry = ttk.Entry(
            frame,
            width=30,
            font=('TkDefaultFont', 9),
            state='readonly'
        )
        entry.insert(0, encrypted_password)
        entry.configure(state='readonly')
        entry.pack(side='left')

        # Simpan data sebagai atribut
        entry.encrypted = encrypted_password
        entry.showing_encrypted = True

        ttk.Button(
            frame,
            text="👁️",
            width=3,
            command=lambda e=entry: self.toggle_password_visibility(e)
        ).pack(side='left', padx=3)

    def toggle_password_visibility(self, entry):
        """Toggle tampilan password"""
        try:
            if entry.showing_encrypted:
                decrypted = decrypt_data(entry.encrypted, get_aes_key(self.master_password))
                self._update_entry(entry, decrypted, 'blue', False)
            else:
                self._update_entry(entry, entry.encrypted, 'black', True)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mendekripsi:\n{str(e)}")

    def _update_entry(self, entry, text, color, is_encrypted):
        """Update tampilan entry"""
        entry.configure(state='normal')
        entry.delete(0, tk.END)
        entry.insert(0, text)
        entry.configure(
            state='readonly',
            foreground=color,
            show='' if is_encrypted else '•'
        )
        entry.showing_encrypted = is_encrypted

    def recovery_password(self):
        """Proses recovery password menggunakan Twilio"""
        try:
            self.recovery_code = str(random.randint(100000, 999999))
            
            # Konfigurasi Twilio (Ganti dengan credential Anda)
            ACCOUNT_SID = 'ubah_akun_sid_anda'
            AUTH_TOKEN = 'ubah_auth_token_anda'
            TWILIO_NUMBER = 'ubah_nomor_twilio_anda'
            TARGET_NUMBER = 'ubah_nomor_target_anda'
            
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            
            client.messages.create(
                body=f'Kode recovery PassLock: {self.recovery_code}',
                from_=TWILIO_NUMBER,
                to=TARGET_NUMBER
            )
            
            self._show_recovery_dialog()
            
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengirim SMS: {str(e)}")

    def _show_recovery_dialog(self):
        """Menampilkan dialog recovery"""
        window = tk.Toplevel(self.root)
        window.title("Password Recovery")
        window.geometry("300x200")
        
        frame = ttk.Frame(window, padding=10)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Kode verifikasi telah dikirim").pack(pady=5)
        
        ttk.Label(frame, text="Masukkan Kode:").pack()
        self.code_entry = ttk.Entry(frame, width=10)
        self.code_entry.pack(pady=5)
        
        ttk.Label(frame, text="Password Baru:").pack()
        self.new_password_entry = ttk.Entry(frame, show="•")
        self.new_password_entry.pack(pady=5)
        
        ttk.Button(
            frame,
            text="Verifikasi",
            command=self._verify_recovery_code
        ).pack(pady=10)

    def _verify_recovery_code(self):
        """Verifikasi kode recovery"""
        if self.code_entry.get() != self.recovery_code:
            messagebox.showerror("Gagal", "Kode verifikasi salah!")
            return

        new_password = self.new_password_entry.get()
        with open("master_password.hash", "w") as f:
            f.write(hash_password(new_password))
            
        messagebox.showinfo("Berhasil", "Password berhasil direset!")
        self.setup_login_ui()

    def clear_widgets(self):
        """Membersihkan semua widget"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def open_biometric(self):
        BiometricScreen(self.root, self.biometric_success)
    
    def biometric_success(self):
        messagebox.showinfo("Berhasil", "Autentikasi biometrik berhasil.")

    def open_add_password_dialog(self):
        AddPasswordDialog(self.root, self.master_password)
        