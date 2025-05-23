# PassLock Pro

**PassLock Pro** adalah aplikasi penyimpanan kredensial login dengan **enkripsi ganda** menggunakan **SHA-256 dan AES**, dilengkapi dengan **simulasi autentikasi biometrik**, serta **fitur pemulihan darurat** melalui email. Dirancang dengan antarmuka sederhana menggunakan **Tkinter**, aplikasi ini cocok untuk pengguna yang menginginkan keamanan data lokal tanpa kompleksitas cloud.

---

## 🚀 Fitur Utama

- 🔐 **Enkripsi Ganda (SHA-256 + AES)**
  - Password akun disimpan secara terenkripsi menggunakan AES (CBC), dengan kunci yang dihasilkan dari hash SHA-256 master password.

- 🧬 **Simulasi Biometrik**
  - Autentikasi tambahan berbasis simulasi sidik jari sebelum mengakses fitur utama.

- 📩 **Pemulihan Darurat**
  - Fitur pengiriman kode pemulihan terenkripsi via email (SMTP).

- 📝 **Manajemen Kredensial**
  - Tambah, lihat, dan simpan akun (layanan, username, password) secara lokal dan terenkripsi.

---

## 🛠️ Teknologi yang Digunakan

- 🐍 Python 3.11
- 🪟 Tkinter (GUI)
- 🔐 PyCryptodome (AES Encryption)
- 📧 smtplib (SMTP Email Sender)
- 🗃️ SQLite (Database lokal opsional)

---

## 📁 Struktur Folder

```

PassLockPro/
├── app/
│   ├── hash\_module.py
│   ├── encryption\_module.py
│   ├── password\_manager.py
│   ├── biometric\_auth.py
│   ├── recovery\_module.py
│   └── config.py
├── ui/
│   ├── main\_window\.py
│   ├── add\_password\_dialog.py
│   ├── recovery\_dialog.py
│   ├── biometric\_screen.py
│   └── assets/
├── data/
│   └── credentials.db
├── keys/
│   ├── master.key
│   └── recovery.key
├── logs/
│   └── access\_log.txt
├── main.py
├── requirements.txt
└── README.md

````

---

## 📦 Instalasi & Menjalankan

1. **Clone repo**
   ```bash
   git clone https://github.com/username/passlock-pro.git
   cd passlock-pro
````

2. **Install dependency**

   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**

   ```bash
   python main.py
   ```

---

## ⚠️ Catatan Penting

* File `config.ini` untuk email **jangan dipush ke publik**, karena berisi informasi kredensial.
* Aplikasi hanya menyimpan data **secara lokal**, tidak terhubung ke internet/cloud.

---

## 📜 Lisensi

MIT License © 2025 – Rey & Team

```

---

Kalau kamu ingin aku bantu juga membuat versi bahasa Inggris atau template badge GitHub (Build, Python Version, dsb.), tinggal bilang aja!
```
