from data.storage import transaksi

def laporan_pengeluaran_boros():
    print()
    print("======== Daftar Pengeluaran =========")
    
    batas_boros = 1000000 
    
    for item in transaksi:
        jumlah = item["jumlah"]
        
        if jumlah > batas_boros:
            kategori = item["kategori"]
            
            print("\nPeringatan Pengeluaran Boros: ")
            print(f" - Kategori: {kategori}")
            print(f" - Jumlah: Rp.{jumlah:}")
    print()
    print("=" * 38)