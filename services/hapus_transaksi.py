from data.storage import transaksi, daftar_kategori
from services.tampilan_transaksi import tampilan_transaksi

def hapus_transaksi():
    
    tampilan_transaksi()
    print()
    
    nomor = int(input("Masukkan nomor dari Daftar Transaksi yang ingin dihapus: "))
    
    while True:
        if nomor:
            kategori_dihapus = transaksi[nomor - 1]['kategori']
            del transaksi[nomor - 1]

            if not any(t['kategori'] == kategori_dihapus for t in transaksi):
                daftar_kategori.remove(kategori_dihapus)
            
            print("Telah berhasil dihapus.\n")
            break
        else:
            print("Nomor pada daftar transaksi tidak valid, Silahkan masukkan nomor yang benar.")