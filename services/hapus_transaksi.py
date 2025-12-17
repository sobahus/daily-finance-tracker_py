from data.storage import transaksi, daftar_kategori
from services.tampilan_transaksi import tampilan_transaksi

def hapus_transaksi():
    
    tampilan_transaksi()
    print()
        
    while True:
        try:
            nomor = int(input("Masukkan nomor dari Daftar Transaksi yang ingin dihapus: "))

            if nomor >= 1 and nomor <= len(transaksi):
                kategori_dihapus = transaksi[nomor - 1]['kategori']
                del transaksi[nomor - 1]
                
                if not any(trx["kategori"] == kategori_dihapus for trx in transaksi):
                    daftar_kategori.remove(kategori_dihapus)
                
                print(f"kategori: {kategori_dihapus} dari Daftar Transaksi Telah berhasil dihapus.\n")
                break
            else:
                print("Nomor tidak valid, silahkan coba lagi.\n")
                
        except ValueError:
            print("Field ini tidak boleh kosong dan Harus berupa angka.\n") 