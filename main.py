from services.input_transaksi import input_transaksi
from services.edit_transaksi import edit_transaksi
from services.hapus_transaksi import hapus_transaksi
from services.tampilan_transaksi import tampilan_transaksi
from services.tampilan_per_kategori import tampilan_per_kategori
from services.laporan_transaksi import laporan_pengeluaran_boros

def main():
    
    print('''                                                
  ▄▄▄              ▄▄                            
 █▀██  ██  ██▀▀     ██                           
   ██  ██  ██       ██             ▄             
   ██  ██  ██ ▄█▀█▄ ██ ▄███▀ ▄███▄ ███▄███▄ ▄█▀█▄
   ██▄ ██▄ ██ ██▄█▀ ██ ██    ██ ██ ██ ██ ██ ██▄█▀
   ▀████▀███▀▄▀█▄▄▄▄██▄▀███▄▄▀███▀▄██ ██ ▀█▄▀█▄▄▄                                        
    ''')
    
    while True:
        print("========== Aplikasi Manajemen Keuangan Harian ===========\n")   
        print("1. Tambah Transaksi") 
        print("2. Edit Transaksi") 
        print("3. Hapus Transaksi") 
        print("4. Tampilkan Semua Transaksi") 
        print("5. Tampilkan Transaksi per Kategori") 
        print("6. Deteksi Pengeluaran Boros") 
        print("7. Exit")
        
        try:
            pilihan = int(input("Pilih Opsi : "))
        except ValueError:
            print("Maaf, silahkan masukkan berupa angka")
            continue
            
        match pilihan:
            case 1:
                input_transaksi()
            case 2:
                edit_transaksi()
            case 3:
                hapus_transaksi()
            case 4:
                tampilan_transaksi()
            case 5:
                tampilan_per_kategori()
            case 6:
               laporan_pengeluaran_boros()
            case 7:
                print("Selamat tinggal, have a nice day! XD")
                break
            case _:
                print("Opsi tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()
