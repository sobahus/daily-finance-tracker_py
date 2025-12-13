from data.storage import transaksi, daftar_kategori

def tambah_transaksi(kategori, jumlah, tanggal):
    if jumlah <= 0:
        print("Jumlah harus lebih dari 0.")
        return False           
        
    transaksi.append({
        "kategori": kategori,
        "jumlah": jumlah,
        "tanggal": tanggal
    })
    daftar_kategori.add(kategori)
