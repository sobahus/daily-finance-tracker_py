from data.storage import transaksi, daftar_kategori

def laporan_pengeluaran_boros():
    print("== Daftar Pengeluaran ==")
    
    batas_boros = 1000000
    
    for item in transaksi:
        total = sum(t["jumlah"] for t in transaksi)
        if item["jumlah"] > batas_boros:
            print(f"PERINGATAN KATEGORI BOROS:")
            print(f"{item}: Rp.{total}")
            