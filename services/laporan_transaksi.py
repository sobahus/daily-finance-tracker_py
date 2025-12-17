from data.storage import transaksi

def laporan_pengeluaran_boros():
    print()
    print("======== Daftar Pengeluaran ==========")
    
    batas_boros = 1000000 
        
    if batas_boros > 0:
        print("\nTidak ada pengeluaran boros yang terdeteksi.")
        
    for item in transaksi:
        total_harga = item["jumlah"] * item["harga"]
        
        if total_harga > batas_boros:
            kategori = item["kategori"]
            print("\nPeringatan Pengeluaran Boros: ")
            print(f" - Kategori: {kategori}")
            print(f" - Jumlah: Rp.{total_harga:}")
    print()
    print("=" * 38)
        

