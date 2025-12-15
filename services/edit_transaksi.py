from data.storage import transaksi
from services.tampilan_transaksi import tampilan_transaksi

def edit_transaksi():
    
    tampilan_transaksi()
    nomor = int(input("Masukkan nomor transaksi yang ingin diubah : "))

    if 0 <= nomor <= len(transaksi) - 1:
        kategori_baru = input("Masukkan kategori baru: ")
        jumlah_baru = int(input("Jumlah baru: "))
        tanggal_baru = input("Masukkan tanggal baru DD-MM-YYYY: ")
        
        transaksi[nomor]["kategori"] = kategori_baru
        transaksi[nomor]["jumlah"] = jumlah_baru
        transaksi[nomor]["tanggal"] = tanggal_baru
        
        print("Transaksi berhasil diperbarui.")
    
    