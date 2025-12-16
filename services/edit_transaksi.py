from data.storage import transaksi
from services.tampilan_transaksi import tampilan_transaksi

def edit_transaksi():
    
    tampilan_transaksi()
    nomor = int(input("Masukkan nomor transaksi yang ingin diubah : "))

    if 0 < nomor <= len(transaksi):
        kategori_baru = input("Masukkan kategori baru: ")
        jumlah_baru = int(input("Jumlah baru: "))
        tanggal_baru = input("Masukkan tanggal baru DD-MM-YYYY: ")
        
        transaksi[nomor - 1]["kategori"] = kategori_baru
        transaksi[nomor - 1]["jumlah"] = jumlah_baru
        transaksi[nomor - 1]["tanggal"] = tanggal_baru
        
        print("Transaksi berhasil diperbarui.")
    
    