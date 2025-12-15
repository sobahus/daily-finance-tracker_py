from services.tambah_transaksi import tambah_transaksi

def input_transaksi():      
    
    while True:
        input_kategori = input("Masukkan Kategori: ")
        if input_kategori:
            break
        print("Maaf, field kategori tidak boleh kosong.")
        
    while True:
        try:
            input_jumlah = int(input("Masukkan Jumlah: "))
            if input_jumlah > 0:
                break
            else:
                print("Maaf, Jumlah harus lebih dari 0 dan tidak boleh Kosong.")
        except ValueError:
            print("Maaf Jumlah harus berupa angka dan tidak boleh kosong.")

    while True: 
        input_tanggal = input("Masukkan Tanggal (format: DD-MM-YYYY): ")
        if input_tanggal:
            break
        print("Maaf, field tanggal tidak boleh kosong.")
    
    try:
        tambah_transaksi(input_kategori, input_jumlah, input_tanggal)
        
        print()
        print("Transaksi telah berhasil ditambahkan.")
        print() 
        
    except Exception as err:
        print(f"Terjadi kesalahan: {err}")
        return False 
        


    