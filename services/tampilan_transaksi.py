from data.storage import transaksi, daftar_kategori

def tampilan_transaksi():
    kategori = ["Kategori", "Jumlah", "Tanggal"]

    # Print Tabel dari variabel kategori
    print("No".ljust(10), end = "")
    for col in kategori:
        print(col.ljust(20), end = "")
    print()    
    
    # Menampilkan Tabel row 
    for (idx, row) in enumerate(transaksi, start = 1):
        print(str(idx).ljust(10), end = "")
        
        # Menampilkan kolom per row
        for key in row:
            print(str(row[key]).ljust(20), end = "")
        print()
        
def tampilan_per_kategori():
    pass