from data.storage import transaksi, daftar_kategori
from services.tampilan_transaksi import tampilan_transaksi

def hapus_transaksi():
    
    tampilan_transaksi()
    print()
        
    while True:
        try:
            nomor = int(input("Masukkan nomor dari Daftar Transaksi yang ingin dihapus: "))
            if not transaksi:
                print("Belum ada transaksi yang tersedia untuk dihapus.\n")
                return False
    
            if nomor >= 1 and nomor <= len(transaksi):
                indeks = nomor - 1
                kategori_target = transaksi[indeks]["kategori"]
                kategori_item = transaksi[indeks]["item"]
                konfirmasi = input(f"Apakah Anda yakin ingin menghapus transaksi nomor {nomor}? (y/n): ").lower()
                
                if konfirmasi == 'y':
                    cek_sisa_kategori = any(trx["kategori"] == kategori_target for trx in transaksi)
                    transaksi.pop(indeks) 
                    
                    if not cek_sisa_kategori:
                        daftar_kategori.discard(kategori_target)
                        print(f"\nKategori: {kategori_target} telah dihapus dari Daftar Kategori karena tidak ada transaksi tersisa di kategori tersebut.\n")
                        
                    tampilan_transaksi()
                    print(f"\nKategori  : {kategori_target}")
                    print(f"Item      : {kategori_item} \n")
                    print(f"Transaksi pada nomor {nomor} telah berhasil dihapus.\n")
                    return True
                else:
                    print(f"\nPengahapusan transaksi nomor {nomor} dibatalkan.\n")
                    return False

            else:
                print("Nomor tidak valid, silahkan coba lagi.\n")
        except ValueError:
            print("Field ini tidak boleh kosong dan harus berupa angka!\n")
                
