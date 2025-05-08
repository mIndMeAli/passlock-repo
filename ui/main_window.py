import tkinter as tk
from tkinter import messagebox
from app.hash_module import verify_password

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("PassLock Pro - Login")
        self.master.geometry("350x200")
        self.master.resizable(False, False)

        self.label = tk.Label(master, text="Masukkan Master Password")
        self.label.pack(pady=10)

        self.password_entry = tk.Entry(master, show="*", width=30)
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(master, text="Login", command=self.verify_password)
        self.login_button.pack(pady=10)

        self.recovery_button = tk.Button(master, text="Recovery", command=self.recover_account)
        self.recovery_button.pack()

    def verify_password(self):
        password = self.password_entry.get()
        if password == "":
            messagebox.showwarning("Peringatan", "Password tidak boleh kosong!")
        elif verify_password(password):
            messagebox.showinfo("Sukses", "Login berhasil!")
        else:
            messagebox.showerror("Gagal", "Password salah atau belum tersimpan.")


    def recover_account(self):
        messagebox.showinfo("Pemulihan", "Menu recovery masih dalam pengembangan")
