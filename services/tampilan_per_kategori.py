from data.storage import transaksi, daftar_kategori

def tampilan_per_kategori():
    if not daftar_kategori:
        print("\nBelum ada kategori yang tersedia.\n")
        return
    
    print("\n======= Transaksi per Kategori ========\n")
    
    for ktx in sorted(daftar_kategori):
        item_dalam_kategori = [trx for trx in transaksi if trx["kategori"] == ktx]
        
        if not item_dalam_kategori:
            continue
        
        print(f"- {ktx}")
        
        for trx in transaksi:
            if trx["kategori"] == ktx:
                print(f"  •Item: {trx['item']} | Jumlah: {trx['jumlah']} | Harga Satuan: Rp.{trx['harga']} | tanggal: {trx['tanggal']}")
                print(f"   Total Harga dari Kategori {trx['kategori']}: Rp.{trx['jumlah'] * trx['harga']}\n")