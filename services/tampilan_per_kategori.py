from data.storage import transaksi, daftar_kategori

def tampilan_per_kategori():
    if not daftar_kategori:
        print("\nBelum ada kategori yang tersedia.\n")
        return
    
    print("\n======= Transaksi per Kategori ========\n")
    
    for ktx in sorted(daftar_kategori):
        print(f"- {ktx}")
        
        for trx in transaksi:
            if trx["kategori"] == ktx:
                print(f"  • Tanggal: {trx['tanggal']} | Jumlah: Rp {trx['jumlah']}\n")
