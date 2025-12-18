from data.storage import transaksi
from services.tampilan_transaksi import tampilan_transaksi
    
def validasi_input_transaksi(input_validasi, nilai_saat_ini, tipe_data=str):
    while True:
        masukkan_input = input(f"{input_validasi} (tekan Enter untuk tetap menyimpan data lama) :")
        
        if masukkan_input == "":
            return nilai_saat_ini
        
        if tipe_data == str:
            if masukkan_input.isdigit():
                print("\nMaaf, field ini harus berupa teks!\n")                                                
                continue
            return masukkan_input.capitalize()
        elif tipe_data == int:
            try:
                return int(masukkan_input)
            except ValueError:
                print("\nMaaf, field ini harus berupa angka!\n")
                continue              
    
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
            
            kategori_baru = validasi_input_transaksi("Masukkan kategori baru", transaksi[index]["kategori"]).capitalize()
            item_baru = validasi_input_transaksi("Masukkan item baru", transaksi[index]["item"]).capitalize()
            jumlah_baru = validasi_input_transaksi("Jumlah baru", transaksi[index]["jumlah"], int)
            harga_baru = validasi_input_transaksi("Harga satuan baru", transaksi[index]["harga"], int)
            tanggal_baru = validasi_input_transaksi("Masukkan tanggal baru (DD-MM-YYYY)", transaksi[index]["tanggal"])
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
                    return True
                else:
                    print("\nPerubahan dibatalkan.\n")
                    return False
                    
            except ValueError:
                print("Gagal memperbarui transaksi, Input tidak valid.")
        else:
            print("Nomor transaksi yang dimasukkan tidak valid!\n")