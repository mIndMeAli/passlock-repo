# ui/biometric_screen.py

import tkinter as tk
from tkinter import messagebox
import random

class BiometricScreen:
    def __init__(self, parent, on_success):
        self.top = tk.Toplevel(parent)
        self.top.title("Simulasi Autentikasi Biometrik")
        self.on_success = on_success

        self.label = tk.Label(self.top, text="Letakkan jari Anda di pemindai (klik tombol)", font=("Arial", 12))
        self.label.pack(pady=20)

        self.scan_button = tk.Button(self.top, text="Pindai Sidik Jari", command=self.scan_fingerprint, width=20)
        self.scan_button.pack(pady=10)

        self.status_label = tk.Label(self.top, text="", font=("Arial", 10), fg="blue")
        self.status_label.pack(pady=10)

    def scan_fingerprint(self):
        self.status_label.config(text="Memindai sidik jari...")
        self.top.after(1500, self.check_result)

    def check_result(self):
        success = random.random() < 0.9

        if success:
            self.status_label.config(text="Autentikasi berhasil!", fg="green")
            messagebox.showinfo("Berhasil", "Biometrik dikenali. Anda masuk.")
            self.top.destroy()
            self.on_success()
        else:
            self.status_label.config(text="Autentikasi gagal. Coba lagi.", fg="red")
            messagebox.showerror("Gagal", "Biometrik tidak dikenali.")