from data.storage import transaksi
from services.tampilan_transaksi import tampilan_transaksi
from utils.validasi_input import validasi_input_transaksi
    
def edit_transaksi():
    tampilan_transaksi()
    
    while True:
        try:
            nomor = int(input("Masukkan nomor transaksi yang ingin diubah : "))
        except ValueError:
            print(f"Maaf, Bagian ini tidak boleh kosong dan harus berupa angka.\n")
            continue
        
        if 0 < nomor <= len(transaksi):
            index = nomor - 1
            kategori = transaksi[index]["kategori"]
            item = transaksi[index]["item"]
            jumlah = transaksi[index]["jumlah"]
            harga = transaksi[index]["harga"]
            tanggal = transaksi[index]["tanggal"]
            
            kategori_baru = validasi_input_transaksi("Masukkan kategori baru (tekan Enter untuk tetap menyimpan data lama) : ", kategori).capitalize()
            item_baru = validasi_input_transaksi("Masukkan item baru (tekan Enter untuk tetap menyimpan data lama) : ", item).capitalize()
            jumlah_baru = validasi_input_transaksi("Jumlah baru (tekan Enter untuk tetap menyimpan data lama) : ", jumlah, int)
            harga_baru = validasi_input_transaksi("Harga satuan baru (tekan Enter untuk tetap menyimpan data lama) : ", harga, int)
            tanggal_baru = validasi_input_transaksi("Masukkan tanggal baru (DD-MM-YYYY) (tekan Enter untuk tetap menyimpan data lama) : ", tanggal)
            konfirmasi = input("Apakah yakin ingin mengubah transaksi ini? (y/n): ")
            
            try:
                if konfirmasi.lower() == 'y':
                    transaksi[index].update({
                        "kategori": kategori_baru,
                        "item": item_baru,
                        "jumlah": jumlah_baru,
                        "harga": harga_baru,
                        "tanggal": tanggal_baru
                    })
                    
                    print("\nTransaksi berhasil diperbarui.\n")
                    tampilan_transaksi()
                    print()
                    return True
                else:
                    print("\nPerubahan dibatalkan.\n")
                    return False
            except ValueError:
                print("\nGagal memperbarui transaksi, Input tidak valid.\n")
        elif not transaksi:
            print("\nBelum ada transaksi yang tersedia untuk diubah.\n")
            return False
        print("\nNomor transaksi yang dimasukkan tidak valid!\n")