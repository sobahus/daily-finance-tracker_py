from data.storage import transaksi, daftar_kategori

def tambah_transaksi():
    while True:
        input_kategori = input("Masukkan Kategori: ").capitalize()
        
        if input_kategori:
            break
        print("Maaf, field kategori tidak boleh kosong.")

    while True:
        try:
            input_item = input("Masukkan nama Barang/Item: ").capitalize()
            
            if input_item:
                break
            print("Maaf, field item tidak boleh kosong.")
        except ValueError:
            print("Maaf, field item tidak boleh kosong.")
        
    while True:
        try:
            input_jumlah = int(input("Masukkan Jumlah: "))
            
            if input_jumlah > 0:
                break
            print(f"Maaf, jumlah harus lebih dari {input_jumlah}")
        except ValueError:
            print("Maaf, field harus berupa angka desimal dan tidak boleh kosong.")
            
    while True:
        try:
            input_harga = int(input("Masukkan Harga: "))
            
            if input_harga > 0:
                break
            print(f"Maaf, harga harus lebih dari {input_harga}")
        except ValueError:
            print("Maaf, field harus berupa angka desimal dan tidak boleh kosong.")

    while True:
        input_tanggal = input("Masukkan Tanggal (format: DD-MM-YYYY): ")
        
        if input_tanggal:
            break
        print("Maaf, field tanggal tidak boleh kosong.")

    try:
        transaksi.append({
            "kategori": input_kategori,
            "item": input_item,
            "jumlah": input_jumlah,
            "harga": input_harga,
            "tanggal": input_tanggal,
        })
        daftar_kategori.add(input_kategori)

        print()
        print("Transaksi telah berhasil ditambahkan.")
        print() 
        return True
    
    except Exception as err:
        print(f"Terjadi kesalahan saat menyimpan data: {err}")
        return False