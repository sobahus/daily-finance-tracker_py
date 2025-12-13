from services.input_transaksi import input_transaksi
from services.tampilan_transaksi import tampilan_transaksi

def tampilkan_transaksi():
    while True:
        print("== Aplikasi Manajemen Keuangan Harian ==")   
        print("1. Tambah Transaksi") 
        print("2. Tampilkan Semua Transaksi") 
        print("3. Tampilkan Transaksi per Kategori") 
        print("4. Hitung Total per Kategori") 
        print("5. Exit")
        
        try:
            pilihan = int(input("Pilih opsi (1-5): "))
        except ValueError:
            print("Maaf, silahkan masukkan berupa angka antara 1-5.")
            continue
            
        match pilihan:
            case 1:
                input_transaksi()
                continue
            case 2:
                tampilan_transaksi()
                continue
            case 3:
                print("Menampilkan transaksi per kategori...")
                continue
            case 4:
                print("Menghitung total per kategori...")
                continue
            case 5:
                print("Selamat tinggal, have a nice day! XD")
                exit()
            case _:
                print("Opsi tidak valid. Silakan coba lagi.")
                continue
            
        