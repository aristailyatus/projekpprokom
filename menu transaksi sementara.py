class Barang:
    def __init__(self, id_barang, nama_barang, harga_barang, stok_barang):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.harga_barang = harga_barang
        self.stok_barang = stok_barang

# Data awal barang
daftar_barang = [
    Barang(1, "Semen", 10000, 50),
    Barang(2, "Batako", 5000, 100),
    Barang(3, "Batu bata", 3000, 150),
    Barang(4, "Besi beton", 20000, 30), #mau gini tapi pake data barang yang sebelumnya gimana yah
]

def tampilkan_daftar_barang():
    print("=== MENU TRANSAKSI ===")
    print("{:<10} {:<20} {:<15} {:<10}".format("ID Barang", "Nama Barang", "Harga Barang", "Stok Barang"))
    print("-" * 60)
    for barang in daftar_barang:
        print("{:<10} {:<20} {:<15} {:<10}".format(barang.id_barang, barang.nama_barang, barang.harga_barang, barang.stok_barang))

def pilih_barang():
    tampilkan_daftar_barang()
    id_barang = int(input("Masukkan ID barang yang dibeli: "))
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    return id_barang, jumlah_barang

def hitung_total_harga(id_barang, jumlah_barang):
    for barang in daftar_barang:
        if barang.id_barang == id_barang:
            return barang.harga_barang * jumlah_barang
    return 0

def perbarui_stok_barang(id_barang, jumlah_barang):
    for barang in daftar_barang:
        if barang.id_barang == id_barang:
            barang.stok_barang -= jumlah_barang

def menu_transaksi():
    id_barang, jumlah_barang = pilih_barang()

    print("Pilih metode pembayaran:")
    print("1. Cash")
    print("2. Transfer")
    
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        menu_cash(id_barang, jumlah_barang)
    elif pilihan == "2":
        menu_transfer(id_barang, jumlah_barang)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def menu_cash(id_barang, jumlah_barang):
    total_harga = hitung_total_harga(id_barang, jumlah_barang)
    print("Total uang yang harus dibayarkan:", total_harga)
    nominal_uang = int(input("Masukkan nominal uang yang digunakan: "))
    kembalian = nominal_uang - total_harga
    print("Kembalian:", kembalian)

    # Perbarui stok barang setelah transaksi
    perbarui_stok_barang(id_barang, jumlah_barang)

def menu_dashboard_admin():
    # Kode untuk menu Dashboard Admin
    pass

def menu_transfer(id_barang, jumlah_barang):
    print("Menu Transfer Bank")
    print("1. Bank BCA")
    print("2. Bank Mandiri")
    print("3. Bank BNI")
    
    pilihan_bank = input("Masukkan pilihan Bank: ")

    if pilihan_bank == "1":
        transfer("BCA", hitung_total_harga(id_barang, jumlah_barang))
    elif pilihan_bank == "2":
        transfer("Mandiri", hitung_total_harga(id_barang, jumlah_barang))
    elif pilihan_bank == "3":
        transfer("BNI", hitung_total_harga(id_barang, jumlah_barang))
    else:
        print("Pilihan tidak valid")

def transfer(nama_bank, jumlah_uang):
    print(f"Transfer ke nomor rekening {nama_bank} sejumlah {jumlah_uang}")

menu_transaksi()




