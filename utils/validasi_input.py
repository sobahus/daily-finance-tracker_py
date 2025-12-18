def validasi_input_transaksi(input_validasi, nilai_saat_ini=None, tipe_data=str):
    while True:
        masukkan_input = input(f"{input_validasi}")
        
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