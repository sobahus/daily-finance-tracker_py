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
│   └─ storage.py
│
├── services/
│   ├── input_transaksi.py
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
          "kategori": "Minuman",
          "jumlah": 10000,
          "tanggal": "14-12-2025"
      },
      ...
  ]
  ```
- `daftar_kategori` (set): Menyimpan kategori unik transaksi

---

### 📁 services/

#### `input_transaksi.py`

Handle input transaksi baru dari user.

- **Fungsi**: `input_transaksi()`
  - Validasi input kategori (tidak boleh kosong)
  - Validasi input jumlah (harus angka > 0)
  - Validasi input tanggal (format: DD-MM-YYYY)
  - Memanggil `tambah_transaksi()` untuk menyimpan data

#### `tambah_transaksi.py`

Logic untuk menambah transaksi ke storage.

- **Fungsi**: `tambah_transaksi(kategori, jumlah, tanggal)`
  - Append transaksi baru ke list `transaksi`
  - Tambahkan kategori ke `daftar_kategori` (set)

#### `edit_transaksi.py`

Fitur untuk mengubah transaksi yang sudah ada.

- **Fungsi**: `edit_transaksi()`
  - Tampilkan semua transaksi
  - User pilih nomor transaksi yang ingin diubah
  - Update data: kategori, jumlah, tanggal
  - Konfirmasi update berhasil

#### `hapus_transaksi.py`

Fitur untuk menghapus transaksi.

- **Fungsi**: `hapus_transaksi()`
  - Tampilkan semua transaksi
  - User pilih nomor transaksi yang ingin dihapus
  - Hapus dari list `transaksi`
  - Jika kategori tidak ada lagi di transaksi, hapus dari `daftar_kategori`

#### `tampilan_transaksi.py`

Menampilkan semua transaksi dalam format tabel.

- **Fungsi**: `tampilan_transaksi()`
  - Header: No | Kategori | Jumlah | Tanggal
  - Loop dengan enumerate untuk numbering
  - Format output dengan `.ljust()` untuk alignment

#### `tampilan_per_kategori.py`

Menampilkan transaksi dikelompokkan per kategori.

- **Fungsi**: `tampilan_per_kategori()`
  - Loop kategori yang di-sort
  - Nested loop untuk transaksi per kategori
  - Format: kategori → daftar transaksi dengan tanggal & jumlah

#### `laporan_transaksi.py`

Deteksi pengeluaran yang boros.

- **Fungsi**: `laporan_pengeluaran_boros()`
  - Batas boros: Rp 1.000.000
  - Loop transaksi dan cek jika jumlah > batas
  - Tampilkan peringatan dengan kategori & jumlah

---

## Konsep Programming yang Digunakan

### 1. **Data Structure**

- **List of Dictionary**: Menyimpan transaksi dengan struktur terorganisir
- **Set**: Menyimpan kategori unik (tidak ada duplikasi)

### 2. **Function & Modular Programming**

- Setiap fitur dipisah ke function berbeda
- Import/Export antar module
- Separation of Concerns (data vs logic vs presentation)

### 3. **Control Flow**

- `match-case` statement untuk menu routing
- `while` loop untuk validasi input
- `if-else` untuk conditional logic

### 4. **Error Handling**

- `try-except` untuk handle input error
- Validasi data sebelum diproses

### 5. **String Formatting**

- `.ljust()` untuk tabel alignment
- f-string untuk output dinamis
- ASCII art untuk UI

### 6. **Nested Loop**

- Loop kategori → loop transaksi per kategori
- Enumerate untuk numbering otomatis

---

## Cara Menjalankan

```bash
python main.py
```

---

## Dependencies

- Python 3.10+ (menggunakan `match-case` statement)
- Tidak ada library external yang dibutuhkan
