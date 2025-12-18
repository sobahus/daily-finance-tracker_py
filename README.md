<h2 style="color: #f5f5f5f; font-weight: bold;">Aplikasi Manajemen Keuangan Harian</h2>

```
Program mencatat Pengeluaran

  - Data transaksi: kategori, jumlah, tanggal.
  - Disimpan ke list of dictionary.
  - Kategori unik disimpan ke set.
  - Fitur:
    - Tambah transaksi.
    - Tampilkan transaksi per kategori (nested loop).
    - Hitung total per kategori (fungsi).
    - Deteksi pengeluaran boros:
      - Jika total kategori > 1.000.000 → tampilkan peringatan.
```

## Struktur Project

```
finance-management/
│
├── main.py
│
├── data/
│   └── storage.py
│
├── services/
│   ├── tambah_transaksi.py
│   ├── edit_transaksi.py
│   ├── hapus_transaksi.py
│   ├── tampilan_transaksi.py
│   ├── tampilan_per_kategori.py
│   └── laporan_transaksi.py
│
└── README.md
```

## Detail Struktur & Fungsi

### 📁 Root Directory

#### `main.py`

File utama yang menjalankan aplikasi.

- **Fungsi**: `main()`
  - Menampilkan ASCII art logo aplikasi
  - Menu interaktif dengan 7 opsi
  - Menggunakan `match-case` untuk routing
  - Import semua fungsi dari services

**Menu Aplikasi:**

1. Tambah Transaksi
2. Edit Transaksi
3. Hapus Transaksi
4. Tampilkan Semua Transaksi
5. Tampilkan Transaksi per Kategori
6. Deteksi Pengeluaran Boros
7. Exit

---

### 📁 data/

#### `storage.py`

Menyimpan data global aplikasi.

**Variable Global:**

- `transaksi` (list of dict): Menyimpan semua data transaksi

  ```python
  [
      {
          "kategori": "Makanan",
          "item": "Nasi Goreng",
          "jumlah": 2,
          "harga": 12000,
          "tanggal": "14-12-2025"
      },
      ...
  ]
  ```

- `daftar_kategori` (set): Menyimpan kategori unik transaksi

  ```python
  {"Makanan", "Minuman", "Transportasi", "Penginapan"}
  ```

---

### 📁 services/

#### `tambah_transaksi.py`

Handle input, validasi, dan tambah transaksi baru ke storage.

- **Fungsi**: `tambah_transaksi()`

  **Validasi Input:**

  - **Kategori** (string): Tidak boleh kosong, auto-capitalize
  - **Item/Barang** (string): Tidak boleh kosong, auto-capitalize
  - **Jumlah** (integer): Harus angka > 0, try-except validation
  - **Harga** (integer): Harus angka > 0, try-except validation
  - **Tanggal** (string): Format DD-MM-YYYY, tidak boleh kosong

  **Proses:**

  - Append transaksi baru ke list `transaksi`
  - Tambahkan kategori ke `daftar_kategori` (set)
  - Error handling dengan try-except
  - Return True jika berhasil, False jika gagal

#### `edit_transaksi.py`

Fitur untuk mengubah transaksi dengan validasi lengkap dan opsi skip.

- **Fungsi Utama**: `edit_transaksi()`
- **Fungsi Helper**: `validasi_input_transaksi(input_validasi, nilai_saat_ini, tipe_data=str)`

  **Fitur Validasi:**

  - **Enter kosong** = mempertahankan data lama (tidak perlu input ulang)
  - Validasi tipe data (string vs integer)
  - String tidak boleh berupa angka
  - Integer harus berupa angka valid
  - Auto-capitalize untuk string

  **Proses:**

  - Tampilkan semua transaksi
  - User pilih nomor transaksi (validasi angka & index valid)
  - Input data baru dengan opsi skip (tekan Enter)
  - **Konfirmasi** sebelum update (y/n)
  - Update dengan `.update()` method
  - Tampilkan hasil update
  - Error handling untuk input tidak valid

#### `hapus_transaksi.py`

Fitur untuk menghapus transaksi dengan konfirmasi dan auto-cleanup kategori.

- **Fungsi**: `hapus_transaksi()`

  **Proses:**

  - Tampilkan semua transaksi
  - User pilih nomor transaksi yang ingin dihapus
  - **Konfirmasi** sebelum hapus (y/n) untuk mencegah kesalahan
  - Cek apakah masih ada transaksi lain dengan kategori yang sama
  - Hapus transaksi dengan `.pop(indeks)`
  - **Auto-cleanup**: Jika tidak ada transaksi tersisa di kategori tersebut:
    - Hapus kategori dari `daftar_kategori` dengan `.discard()`
    - Tampilkan notifikasi kategori dihapus
  - Tampilkan detail transaksi yang dihapus (kategori & item)
  - Error handling untuk input kosong atau tidak valid

#### `tampilan_transaksi.py`

Menampilkan semua transaksi dalam format tabel lengkap dengan perhitungan otomatis.

- **Fungsi**: `tampilan_transaksi()`

  **Struktur Tabel:**

  - Header: No | Kategori | Item | Jumlah | Harga Satuan | Total | Tanggal
  - **Perhitungan otomatis**: Total per item = jumlah × harga satuan
  - **Footer**: Total Pengeluaran (sum semua transaksi)
  - Garis pemisah dengan `-` × panjang_baris

  **Fitur:**

  - Format alignment dengan `.ljust()` untuk kolom rapi
  - Enumerate untuk auto-numbering (start=1)
  - List untuk menyimpan total per item
  - Dynamic column width calculation
  - Menampilkan grand total pengeluaran

#### `tampilan_per_kategori.py`

Menampilkan transaksi dikelompokkan berdasarkan kategori dengan detail lengkap.

- **Fungsi**: `tampilan_per_kategori()`

  **Output Format:**

  - Kategori (sorted alfabetis)
  - Per item dalam kategori:
    - Nama item
    - Jumlah
    - Harga satuan
    - Tanggal
    - **Total harga** (jumlah × harga satuan)

  **Fitur:**

  - **Sorted categories** dengan `sorted()` untuk urutan alfabetis
  - **List comprehension** untuk filter item per kategori
  - Skip kategori yang tidak memiliki transaksi
  - Nested loop: kategori → transaksi dalam kategori
  - Perhitungan total per item
  - Cek jika tidak ada kategori tersedia

#### `laporan_transaksi.py`

Deteksi pengeluaran boros berdasarkan total harga per transaksi.

- **Fungsi**: `laporan_pengeluaran_boros()`

  **Kriteria:**

  - **Batas boros**: Rp 1.000.000 per transaksi
  - **Perhitungan**: total_harga = jumlah × harga satuan

  **Logic:**

  - Hitung total semua transaksi dengan generator expression
  - Jika total < batas → tampilkan "Tidak ada pengeluaran boros"
  - Loop setiap transaksi dan hitung total per item
  - Jika total_harga > 1.000.000 → tampilkan peringatan
  - Tampilkan kategori dan total pengeluaran yang boros

---

## Konsep Programming yang Digunakan

### 1. **Data Structure**

- **List of Dictionary**: Menyimpan transaksi dengan struktur kompleks (kategori, item, jumlah, harga, tanggal)
- **Set**: Menyimpan kategori unik (auto-eliminasi duplikasi)
- **List**: Untuk menyimpan total per item dalam perhitungan

### 2. **Function & Modular Programming**

- **Separation of Concerns**: data, logic, presentation terpisah
- **Import/Export**: antar module dengan `from ... import ...`
- **Helper functions**: `validasi_input_transaksi()` untuk reusable code
- **Main function**: `main()` sebagai entry point

### 3. **Control Flow**

- **Match-case** (Python 3.10+): routing menu yang clean
- **While loop**: validasi input hingga benar
- **If-else**: conditional logic untuk validasi
- **For loop**: iterasi data transaksi
- **Try-except**: error handling

### 4. **Error Handling**

- **Try-except ValueError**: handle input yang bukan angka
- **Validasi ketat**: cek kondisi sebelum proses data
- **Error message**: informasi yang jelas dan spesifik
- **Return value**: True/False untuk status operasi

### 5. **String Formatting & Manipulation**

- **f-string**: output dinamis (`f"Total: Rp.{total}"`)
- **`.ljust()`**: alignment tabel untuk tampilan rapi
- **`.capitalize()`**: format teks otomatis (huruf kapital di awal)
- **`.lower()`**: normalisasi input konfirmasi (y/n)
- **ASCII art**: UI yang menarik di terminal

### 6. **Advanced Python Techniques**

- **Enumerate**: auto-numbering dengan index (`start=1`)
- **Nested loop**: kategori → transaksi per kategori
- **List comprehension**: `[trx for trx in transaksi if trx["kategori"] == ktx]`
- **Generator expression**: `sum(t["jumlah"] * t["harga"] for t in transaksi)`
- **Set operations**: `.add()`, `.discard()` untuk manage kategori
- **Dictionary methods**: `.update()`, `.pop()`, `.append()`
- **Any() function**: `any(trx["kategori"] == ktx for trx in transaksi)`
- **Sorted()**: mengurutkan kategori alfabetis

### 7. **User Experience (UX)**

- **Konfirmasi**: mencegah kesalahan edit/hapus (y/n)
- **Optional input**: tekan Enter untuk skip saat edit
- **Validasi real-time**: langsung cek input user
- **Feedback jelas**: notifikasi berhasil/gagal/dibatalkan
- **Auto-cleanup**: hapus kategori kosong otomatis
- **Dynamic calculation**: total dihitung otomatis

### 8. **Best Practices**

- **DRY Principle**: Don't Repeat Yourself (helper function untuk validasi)
- **Clear naming**: nama variable dan function yang deskriptif
- **Modular code**: setiap file punya tanggung jawab spesifik
- **Input validation**: validasi semua input user
- **Defensive programming**: cek kondisi edge case

## Fitur Unggulan

1. **Validasi Input Lengkap**: Semua input divalidasi dengan ketat
2. **Konfirmasi User**: Mencegah kesalahan edit/hapus yang tidak disengaja
3. **Auto-capitalize**: Format teks otomatis untuk konsistensi
4. **Opsi Skip Input**: Tekan Enter untuk mempertahankan data lama saat edit
5. **Dynamic Category Management**: Auto-hapus kategori jika tidak ada transaksi tersisa
6. **Auto Calculator**: Hitung total pengeluaran otomatis (jumlah × harga)
7. **Tabel Rapi**: Format alignment yang konsisten dan mudah dibaca
8. **Error Handling**: Pesan error yang informatif dan membantu

## Cara Menjalankan

```bash
python main.py
```

atau

```bash
python3 main.py
```

## Dependencies

- Python 3.10+
- Tidak ada library external yang dibutuhkan
- Hanya menggunakan built-in Python modules

## Kontributor

Proyek ini dikembangkan oleh Kelompok 2:

- **M. Sobahus Sururin Ni'am** - (NIM: 054)
- **Atta Arrafi P.H.** - (NIM: 035)
- **Zackaria Noza Alfarel** - (NIM: 034)
- **Khoirul Ikhsan Riadi** - (NIM: 025)

## Rencana Pengembangan Lanjutan Project

```
[ ] Simpan data ke file (JSON/CSV) untuk persistensi data
[ ] Export laporan ke PDF atau Excel
[ ] Filter transaksi berdasarkan range tanggal
[ ] GUI dengan Tkinter/PyQt
[ ] Database integration (SQLite/MySQL/MongoDB)
```

**Happy Ngoding! 🚀**
