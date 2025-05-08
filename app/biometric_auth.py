class BiometricAuthSimulator:
    def __init__(self):
        # Ini bisa diganti dengan logika penyimpanan PIN/gestur
        self.registered_pattern = "12345"  # contoh pola biometrik

    def authenticate(self, input_pattern):
        """
        Fungsi autentikasi biometrik (simulasi).
        Bandingkan input dengan pola yang tersimpan.
        """
        return input_pattern == self.registered_pattern

    def update_pattern(self, new_pattern):
        """
        Update pola biometrik pengguna.
        """
        self.registered_pattern = new_pattern
        # Simpan permanen ke file jika ingin persistensinya