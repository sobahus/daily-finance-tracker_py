from services.tambah_transaksi import tambah_transaksi

def input_transaksi():  
    kategori = input("Kategori:")
    
    try:
        jumlah = int(input("Jumlah:"))
    except ValueError:
        print("Maaf Jumlah harus berupa angka.")
        return False

    tanggal = input("Tanggal:")
    
    try:
        tambah_transaksi(kategori, jumlah, tanggal)
        print("========================================")
        print("Transaksi telah Berhasil ditambahkan.")
        print("========================================\n")
    
    except Exception as err:
        print(f"Terjadi kesalahan: {err}")
        return False 
    


    