def validasi_input_transaksi(input_validasi, data_saat_ini=None, tipe_data=str):
    while True:
        masukkan_input = input(f"{input_validasi}")
        
        if masukkan_input == "":
            if data_saat_ini is not None:
                return data_saat_ini
            else:
                print("\nField ini tidak boleh kosong!\n")
                continue
        elif "," in masukkan_input or "." in masukkan_input:
            print("\nMaaf, bagian ini tidak boleh mengandung koma (,)\n")
            continue
        
        if tipe_data == str:
            if masukkan_input.isdigit():
                print("\nMaaf, bagian ini harus berupa teks!\n")
                continue
            return masukkan_input.capitalize()
        
        elif tipe_data == int:
            try:
                if int(masukkan_input) <= 0:
                    print(f"\nMaaf, angka tidak boleh kurang dari {int(masukkan_input)}\n")
                    continue
                return int(masukkan_input)
            except ValueError:
                print("\nMaaf, bagian ini harus berupa angka!\n")
                continue