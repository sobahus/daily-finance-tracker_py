from data.storage import transaksi
from services.tampilan_transaksi import tampilan_transaksi

def hapus_transaksi():
    
    tampilan_transaksi()
    print()
    
    nomor = int(input("Masukkan nomor dari Daftar Transaksi yang ingin dihapus: "))
    
    while True:
        if nomor:
            del transaksi[nomor - 1]
            
            print("Telah berhasil dihapus.\n")
            break
        else:
            print("Nomor pada daftar transaksi tidak valid, Silahkan masukkan nomor yang benar.")

    
    
        
        
    
        
