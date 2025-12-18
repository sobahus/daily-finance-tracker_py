from data.storage import transaksi, daftar_kategori
from utils.validasi_input import validasi_input_transaksi

def tambah_transaksi():
    input_kategori = validasi_input_transaksi("Masukkan Kategori: ", tipe_data=str)
    input_item = validasi_input_transaksi("Masukkan nama Barang/Item: ", tipe_data=str)
    input_jumlah = validasi_input_transaksi("Masukkan Jumlah: ", tipe_data=int)
    input_harga = validasi_input_transaksi("Masukkan Harga: ", tipe_data=int)
    input_tanggal = validasi_input_transaksi("Masukkan Tanggal (format: DD-MM-YYYY): ", tipe_data=str)
    
    try:
        transaksi.append({
            "kategori": input_kategori,
            "item": input_item,
            "jumlah": input_jumlah,
            "harga": input_harga,
            "tanggal": input_tanggal,
        })
        daftar_kategori.add(input_kategori)

        print()
        print("Transaksi telah berhasil ditambahkan.")
        print() 
        return True
    
    except Exception as err:
        print(f"Terjadi kesalahan saat menyimpan data: {err}")
        return False