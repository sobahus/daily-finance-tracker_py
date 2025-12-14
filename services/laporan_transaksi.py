from data.storage import transaksi, daftar_kategori

def laporan_pengeluaran_boros():
    print("== Daftar Pengeluaran ==")
    
    batas_boros = 1000000 
    
    for item in transaksi:
        if item["jumlah"] > batas_boros:
            kategori = item.get("kategori", "Tidak diketahui")
            total = item["jumlah"]
            print("PERINGATAN KATEGORI BOROS:")
            print(f"Kategori: {kategori} | Jumlah: Rp.{total:,}")