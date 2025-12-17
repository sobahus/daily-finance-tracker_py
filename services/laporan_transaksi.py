from data.storage import transaksi

def laporan_pengeluaran_boros():
    print()
    print("============ Daftar Pengeluaran ============")
    
    batas_boros = 1000000 
    total_transaksi = sum(transaksi["jumlah"] * transaksi["harga"] for transaksi in transaksi)
        
    if batas_boros > total_transaksi:
        print("\nTidak ada pengeluaran boros yang terdeteksi.")
        
    for item in transaksi:
        total_harga = item["jumlah"] * item["harga"]
        
        if total_harga > batas_boros:
            kategori = item["kategori"]
            print("\nPeringatan Pengeluaran Boros: ")
            print(f"- Kategori: {kategori}")
            print(f"- Total Pengeluaran: Rp.{total_harga:}")
    print()
    print("=" * 44)
        

