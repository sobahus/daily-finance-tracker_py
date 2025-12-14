import json
from data.storage import transaksi, daftar_kategori

def tambah_transaksi(kategori, jumlah, tanggal):
    transaksi.append({
        "kategori": kategori,
        "jumlah": jumlah,
        "tanggal": tanggal,
    })
    daftar_kategori.add(kategori)
