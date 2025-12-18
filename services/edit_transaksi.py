from data.storage import transaksi
from services.tampilan_transaksi import tampilan_transaksi
    
def validasi_input_transaksi(input_validasi, nilai_saat_ini, tipe_data=str):
    while True:
        input_validasi = input(f"{input_validasi}baru (tekan Enter untuk tetap menyimpan data lama) :")
        
        if input_validasi == "":
            return nilai_saat_ini
        else:
            try:
                if tipe_data == int:
                    return int(input_validasi)
                else:
                    return input_validasi
                
            except ValueError:
                print("Input tidak valid!")
    
def edit_transaksi():
    tampilan_transaksi()
    
    while True:
        try:
            nomor = int(input("Masukkan nomor transaksi yang ingin diubah : "))
        except ValueError:
            print(f"Maaf, field ini tidak boleh kosong dan harus berupa angka.\n")
            continue
        
        if 0 < nomor <= len(transaksi):
            index = nomor - 1
            
            kategori_baru = validasi_input_transaksi("Masukkan kategori ", transaksi[index]["kategori"]).capitalize()
            item_baru = validasi_input_transaksi("Masukkan item ", transaksi[index]["item"]).capitalize()
            jumlah_baru = validasi_input_transaksi("Jumlah ", transaksi[index]["jumlah"], int)
            harga_baru = validasi_input_transaksi("Harga satuan ", transaksi[index]["harga"], int)
            tanggal_baru = validasi_input_transaksi("Masukkan tanggal DD-MM-YYYY ", transaksi[index]["tanggal"])
            konfirmasi = input("Apakah yakin ingin mengubah transaksi ini? (y/n): ")
            
            try:
                if kategori_baru != "":
                    transaksi[index]["kategori"] = kategori_baru
                
                if item_baru != "":
                    transaksi[index]["item"] = item_baru
                
                if jumlah_baru != "":
                    transaksi[index]["jumlah"] = jumlah_baru

                if harga_baru != "":
                    transaksi[index]["harga"] = harga_baru

                if tanggal_baru != "":
                    transaksi[index]["tanggal"] = tanggal_baru
                
                if konfirmasi.lower() == 'y':
                    print("\nTransaksi berhasil diperbarui.\n")
                    tampilan_transaksi()
                    return True
                else:
                    print("Perubahan dibatalkan.")
                    return False
                    
            except ValueError:
                print("Gagal memperbarui transaksi, Input tidak valid.")
        else:
            print("Nomor transaksi yang dimasukkan tidak valid!\n")