from services.tambah_transaksi import tambah_transaksi
from data.storage import daftar_kategori

def input_transaksi():      
    
    while True:
        kategori = input("Masukkan Kategori: ")
        if kategori:
            break
        print("Maaf, field kategori tidak boleh kosong.")
        
    while True:
        try:
            jumlah = int(input("Masukkan Jumlah: "))
            if jumlah > 0:
                break
            else:
                print("Maaf, Jumlah harus lebih dari 0 dan tidak boleh Kosong.")
        except ValueError:
            print("Maaf Jumlah harus berupa angka dan tidak boleh kosong.")

    while True: 
        tanggal = input("Masukkan Tanggal (format: DD/MM/YYYY): ")
        if tanggal:
            break
        print("Maaf, field tanggal tidak boleh kosong.")
    
    try:
        tambah_transaksi(kategori, jumlah, tanggal)
        daftar_kategori.add(kategori)
        
        print()
        print("=== Transaksi telah berhasil ditambahkan. ===")
        print() 
        
    except Exception as err:
        print(f"Terjadi kesalahan: {err}")
        return False 
        


    