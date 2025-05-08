import tkinter as tk
from tkinter import ttk
from app.password_manager import PasswordManager

class DashboardWindow(tk.Toplevel):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.parent = parent
        self.username = username
        self.pm = PasswordManager(username)
        self.title(f"PassLock Pro - Dashboard ({username})")
        self.geometry("800x600")
        self._setup_ui()
        self._load_credentials()

    def _setup_ui(self):
        self.tree = ttk.Treeview(self, columns=("Service", "Username", "Password"), show="headings")
        self.tree.heading("Service", text="Layanan")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        
        self.btn_add = ttk.Button(self, text="Tambah", command=self.open_add_dialog)
        self.btn_delete = ttk.Button(self, text="Hapus", command=self.delete_credential)
        self.btn_logout = ttk.Button(self, text="Logout", command=self.logout)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.btn_add.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_delete.pack(side=tk.LEFT, padx=10)
        self.btn_logout.pack(side=tk.RIGHT, padx=10, pady=10)

    def _load_credentials(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        credentials = self.pm.get_credentials()
        for service, username, password in credentials:
            self.tree.insert("", "end", values=(service, username, password))

    def open_add_dialog(self):
        from ui.dialog_windows import AddCredentialDialog
        AddCredentialDialog(self, self.pm)

    def delete_credential(self):
        selected = self.tree.selection()
        if not selected:
            return
        service = self.tree.item(selected[0])['values'][0]
        self.pm.delete_credential(service)
        self._load_credentials()

    def logout(self):
        self.destroy()
        self.parent.deiconify()