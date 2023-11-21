class Toko:
    def __init__(self):
        self.metode_pembayaran = ["Cash", "Transfer"]
        self.array_metode_pengiriman = ["JNE", "Tiki"]
        self.data_toko = {"nama_toko": "", "alamat_toko": "", "nomor_telepon": ""}

    def atur_informasi_toko(self):
        print("=== ATUR INFORMASI TOKO ===")
        self.data_toko.update({
            "nama_toko": input("Masukkan Nama Toko: "),
            "alamat_toko": input("Masukkan Alamat Toko: "),
            "nomor_telepon": input("Masukkan Nomor Telepon Toko: "),
        })
        print("Informasi toko berhasil diatur.")

    def tambah_metode_pembayaran(self):
        print("=== ATUR METODE PEMBAYARAN ===")
        metode_baru = input("Masukkan Metode Pembayaran Baru: ")
        self.metode_pembayaran.append(metode_baru)
        print(f"Metode pembayaran '{metode_baru}' berhasil ditambahkan.")

    def tambah_metode_pengiriman(self):
        print("=== ATUR METODE PENGIRIMAN ===")
        metode_pengiriman_baru = input("Masukkan Metode Pengiriman Baru: ")
        self.array_metode_pengiriman.append(metode_pengiriman_baru)
        print(f"Metode pengiriman '{metode_pengiriman_baru}' berhasil ditambahkan.")

    def tampilkan_informasi_toko(self):
        print("=== INFORMASI TOKO ===")
        for key, value in self.data_toko.items():
            print(f"{key.capitalize()}: {value}")
        print()

    def tampilkan_menu_pengaturan_toko(self):
        while True:
            print("=== MENU PENGATURAN TOKO ===")
            print("1. Atur Informasi Toko")
            print("2. Metode Pembayaran")
            print("3. Metode Pengiriman")
            print("4. Tampilkan Informasi Toko")
            print("5. Kembali ke Dashboard Admin")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.atur_informasi_toko()
            elif pilihan == "2":
                self.tambah_metode_pembayaran()
            elif pilihan == "3":
                self.tambah_metode_pengiriman()
            elif pilihan == "4":
                self.tampilkan_informasi_toko()
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

toko = Toko()
toko.tampilkan_menu_pengaturan_toko()



