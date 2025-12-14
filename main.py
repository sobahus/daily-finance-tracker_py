from services.input_transaksi import input_transaksi
from services.tampilan_transaksi import tampilan_transaksi
from services.hapus_transaksi import hapus_transaksi
from services.laporan_transaksi import laporan_pengeluaran_boros
from services.tampilan_per_kategori import tampilan_per_kategori

def main():
    while True:
        print("== Aplikasi Manajemen Keuangan Harian ==")   
        print("1. Tambah Transaksi") 
        print("2. Tampilkan Semua Transaksi") 
        print("3. Hapus Transaksi") 
        print("4. Tampilkan Transaksi per Kategori") 
        print("5. Deteksi Pengeluaran Boros") 
        print("6. Exit")
        
        try:
            pilihan = int(input("Pilih Opsi : "))
        except ValueError:
            print("Maaf, silahkan masukkan berupa angka")
            continue
            
        match pilihan:
            case 1:
                input_transaksi()
            case 2:
                tampilan_transaksi()
            case 3:
                hapus_transaksi()
            case 4:
                tampilan_per_kategori()
            case 5:
               laporan_pengeluaran_boros()
            case 6:
                print("Selamat tinggal, have a nice day! XD")
                break
            case _:
                print("Opsi tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()
