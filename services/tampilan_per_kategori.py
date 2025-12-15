from data.storage import transaksi, daftar_kategori

def tampilan_per_kategori():
    if not daftar_kategori:
        print("Belum ada kategori yang tersedia.")
        return
    
    print("\n======= Transaksi per Kategori ========\n")
    
    for ktx in sorted(daftar_kategori):
        print(f"- {ktx}")
        ditemukan = False
        
        for trx in transaksi:
            if trx["kategori"] == ktx:
                print(f"  • Tanggal: {trx['tanggal']} | Jumlah: Rp {trx['jumlah']}")
                ditemukan = True

        if not ditemukan:
            print("  (Tidak ada transaksi pada kategori ini)") 
        print()