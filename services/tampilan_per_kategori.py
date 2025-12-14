from data.storage import daftar_kategori

def tampilan_per_kategori():
    if not daftar_kategori:
        print("Belum ada kategori yang tersedia.")
        return
    
    # Looping untuk menampilkan semua data kategori
    print("\nDaftar Kategori Transaksi:")
    for idx, kategori in enumerate(daftar_kategori, start=1):
        print(f"{idx}. {kategori}") 
    print()   
    