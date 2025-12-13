from data.storage import transaksi, daftar_kategori

def hapus_transaksi():
    print("Fungsi hapus transaksi dipanggil.")
    
    transaksi.pop([])
