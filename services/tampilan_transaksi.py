from data.storage import transaksi

def tampilan_transaksi():
    kategori = ["Kategori", "Jumlah", "Tanggal"]

    print("===================== Daftar Transaksi =======================\n")
    
    # Menampilkan Tabel dengan header dengan kolom
    print("No".ljust(10), end = "")
    for col in kategori:
        print(col.ljust(20), end = "")
    print()    
    
    # Menampilkan Tabel dengan row
    for (idx, row) in enumerate(transaksi, start=1):
        print(str(idx).ljust(10), end = "")
        
        # Menampilkan kolom per row
        for key in row:
            print(str(row[key]).ljust(20), end = "")
        print()
    print()
    print("=" * 62)