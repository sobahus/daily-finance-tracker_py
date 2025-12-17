from data.storage import transaksi

def tampilan_transaksi():
    kategori = ["Kategori", "item", "Jumlah", "Harga Satuan", "Total", "Tanggal"]
    list_total_per_item = []
    

    print("============================ Daftar Transaksi ==================================\n")
    
    # Menampilkan No di Header Tabel 
    panjang_baris = len(kategori) * 16 + 6
    print("-" * panjang_baris)
    print("No".ljust(4), end="")
    
    # Perulangan untuk menampilkan header tabel
    for item in kategori:
        print(item.ljust(16), end="")
    print()  
    print("-" * panjang_baris)  
    
    # Menampilkan Tabel dengan row
    for (idx, row) in enumerate(transaksi, start=1):
        total_item = row["jumlah"] * row["harga"]
        list_total_per_item.append(total_item)
        
        # Gap/ jarak antar kolom
        print(str(idx).ljust(4), end="")
        
        print(str(row["kategori"]).ljust(16), end="")
        print(str(row["item"]).ljust(16), end="")
        print(str(row["jumlah"]).ljust(16), end="")
        
        harga_satuan_format = str(row["harga"])
        print(harga_satuan_format.ljust(16), end="")
        
        total_item_format = str(total_item)
        print(total_item_format.ljust(16), end="")
        
        print(str(row["tanggal"]), end="")
        print()
        
    # Menampilkan footer Table buat Hasil Total Semua
    print("-" * panjang_baris)
    print(f"Total Pengeluaran: Rp {sum(list_total_per_item)}")
    print("-" * panjang_baris)