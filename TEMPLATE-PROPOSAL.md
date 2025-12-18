# PROPOSAL PROYEK BERBASIS PEMBELAJARAN (PBL)

## Algoritma & Pemrograman (Python)

## 1. IDENTITAS KELOMPOK

### Nama Kelompok:

- **Kelompok:** Kelompok 2

### Anggota & NIM:

- **Nama:** M. Sobahus Sururin Ni'am | **NIM:** (054)
- **Nama:** Atta Arrafi P.H. | **NIM:** (NIM: 035)
- **Nama:** Zackaria Noza Alfarel | **NIM:** (NIM: 043)
- **Nama:** Khoirul Ikhsan Riadi| **NIM:** (NIM: 025)

### Dosen Pengampu:

- **Nama Dosen:** Uce Indahyanti, M.Kom
- **Mata Kuliah:** Algoritma & Pemrograman
- **Program Studi:** Informatika
- **Universitas:** Universitas Muhammadiyah Sidoarjo

### Judul Proyek:

#### Aplikasi Manajemen Keuangan Harian Berbasis Python

## 2. LATAR BELAKANG & DESKRIPSI MASALAH

### 2.1 Latar Belakang Masalah

Dalam kehidupan sehari-hari, banyak orang kesulitan mengelola keuangan mereka dengan baik. Pengeluaran yang tidak terkontrol sering terjadi karena:

- Tidak adanya pencatatan transaksi yang terstruktur
- Sulit melacak pengeluaran per kategori (makanan, transportasi, hiburan, dll)
- Tidak ada sistem peringatan untuk pengeluaran yang berlebihan
- Kesulitan menganalisis pola pengeluaran

Untuk mengatasi masalah ini, diperlukan sebuah aplikasi yang dapat membantu pengguna mencatat, mengelola, dan menganalisis pengeluaran harian mereka dengan mudah dan efisien.

### 2.2 Deskripsi Masalah

Program yang akan dibuat harus mampu:

- Menerima input pengeluaran dari pengguna (kategori, jumlah, tanggal)
- Menyimpan data transaksi secara terstruktur
- Menampilkan transaksi berdasarkan kategori
- Menghitung total pengeluaran per kategori
- Mendeteksi dan memberikan peringatan jika ada kategori pengeluaran yang mencapai batas wajar (melebihi Rp 1.000.000)

### 2.3 Tujuan Pembuatan Program

1. **Tujuan Umum:**

   - Membuat aplikasi yang memudahkan pengguna dalam mengelola keuangan harian

2. **Tujuan Khusus:**
   - Memahami dan menerapkan konsep algoritma & pemrograman Python (loop, kondisi, fungsi, struktur data)
   - Mengimplementasikan input/output yang interaktif
   - Menggunakan struktur data yang tepat untuk menyimpan dan mengolah data
   - Membuat program yang modular dan mudah dimaintain
   - Menerapkan validasi input untuk meningkatkan keandalan program

---

## 3. ANALISIS KEBUTUHAN PROGRAM

### 3.1 Persyaratan Program

Program ini **minimal harus menggunakan:**

#### Input/Output

- Input data transaksi dari pengguna (kategori, jumlah uang, tanggal)
- Output data yang ditampilkan ke konsol dengan format yang rapi
- Menu interaktif untuk memilih fitur program

#### If–Else dan Operator Logika

- Kondisi untuk validasi input pengguna
- Kondisi untuk pengecekan kategori yang sudah ada
- Operator logika (`and`, `or`, `not`) untuk pengecekan kondisi ganda
- Kondisi untuk mendeteksi pengeluaran boros (jika total > Rp 1.000.000)

#### Perulangan (Loop) & Minimal 1 Nested Loop

- Loop untuk menampilkan menu utama hingga pengguna memilih exit
- Loop untuk menavigasi daftar transaksi
- **Nested Loop:** Perulangan dalam perulangan untuk menampilkan transaksi per kategori:
  ```
  untuk setiap kategori:
    untuk setiap transaksi:
      tampilkan transaksi jika kategorinya sesuai
  ```

#### Fungsi (Modular, Minimal 2 Fungsi Buatan)

Fungsi-fungsi yang dibuat:

- `tambah_transaksi()` - Menambahkan transaksi baru
- `edit_transaksi()` - Mengubah data transaksi
- `hapus_transaksi()` - Menghapus transaksi
- `tampilan_transaksi()` - Menampilkan semua transaksi
- `tampilan_per_kategori()` - Menampilkan transaksi per kategori
- `laporan_pengeluaran_boros()` - Mendeteksi pengeluaran berlebihan
- `hitung_total_kategori()` - Menghitung total per kategori

#### Struktur Data (List + Minimal 1 Lagi)

- **List:** Menyimpan daftar transaksi (list of dictionary)
  ```python
  transaksi = [
    {"kategori": "Makanan", "jumlah": 50000, "tanggal": "2025-01-15"},
    {"kategori": "Transportasi", "jumlah": 20000, "tanggal": "2025-01-15"}
  ]
  ```
- **Set:** Menyimpan kategori unik (untuk menghindari duplikasi)
  ```python
  kategori_unik = {"Makanan", "Transportasi", "Hiburan", "Kesehatan"}
  ```
- **Dictionary:** Menyimpan data per transaksi dan hasil perhitungan

### 3.2 Kebutuhan Tambahan

- **Validasi Input:** Memastikan input berupa angka yang valid
- **Persistensi Data:** Menyimpan data ke file (opsional)
- **User Interface:** Menu yang user-friendly dan mudah digunakan
- **Error Handling:** Menangani error input pengguna

---

## 4. DESAIN SOLUSI

### 4.1 Flowchart Sistem

```
┌─────────────────────────┐
│     MULAI PROGRAM       │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  TAMPILKAN MENU UTAMA   │
└────────────┬────────────┘
             │
             ▼
   ┌─────────────────┐
   │ Pilih Opsi Menu │
   └────────┬────────┘
            │
    ┌───────┴───────────────────────────────────────┐
    │                                               │
    ▼                ▼              ▼          ▼     ▼
 Opsi 1        Opsi 2-4        Opsi 5      Opsi 6  Opsi 7
 (Tambah)     (Edit/Hapus)   (Per Kat)   (Laporan)(Exit)
    │             │              │          │      │
    ▼             ▼              ▼          ▼      ▼
 Input Kat    Pilih Transaksi  Nested    Deteksi  ┌──────────┐
 & Jumlah     & Update Data    Loop +    Boros &  │  EXIT    │
    │             │            Hitung    Peringat │ PROGRAM  │
    │             │              │          │     └──────────┘
    └─────┬───────┴──────────────┴──────────┘
          │
          ▼
 ┌───────────────────────┐
 │ Kembali ke Menu Utama?│
 └───────────┬───────────┘
             │
        ┌────┴─────┐
        │           │
       Ya          Tidak
        │           │
        ▼           ▼
    [Ulang]   [Exit Program]
```

### 4.2 Alur Program Langkah Demi Langkah

1. **Inisialisasi Program**

   - Program dimulai dengan menampilkan ASCII art dan judul
   - Inisialisasi list transaksi kosong dan set kategori kosong
   - Load data dari storage jika ada

2. **Tampilkan Menu Utama**

   - Tampilkan 7 opsi menu kepada pengguna
   - Tunggu input dari pengguna (1-7)

3. **Proses Input Pengguna**

   - **Opsi 1 (Tambah):** Input kategori, jumlah, tanggal → Validasi → Simpan ke list
   - **Opsi 2 (Edit):** Tampilkan transaksi → Pilih ID → Update data
   - **Opsi 3 (Hapus):** Tampilkan transaksi → Pilih ID → Hapus dari list
   - **Opsi 4 (Tampilkan Semua):** Loop melalui list dan tampilkan semua transaksi
   - **Opsi 5 (Per Kategori):** Nested loop - untuk setiap kategori, tampilkan transaksinya
   - **Opsi 6 (Laporan):** Hitung total per kategori, deteksi jika > Rp 1.000.000, tampilkan peringatan
   - **Opsi 7 (Exit):** Keluar dari program

4. **Kembali ke Menu**
   - Setelah setiap operasi selesai, kembali ke langkah 2

---

## 5. IMPLEMENTASI PROGRAM

### 5.1 Struktur Folder & File

```
finance-management/
├── main.py                  # File utama dengan menu interaktif
├── data/
│   └── storage.py          # Fungsi menyimpan & load data
├── services/
│   ├── tambah_transaksi.py
│   ├── edit_transaksi.py
│   ├── hapus_transaksi.py
│   ├── tampilan_transaksi.py
│   ├── tampilan_per_kategori.py
│   └── laporan_transaksi.py
└── utils/
    └── validasi_input.py    # Fungsi validasi input
```

### 5.2 Penjelasan Fungsi-Fungsi Utama

#### **`tambah_transaksi()`**

- Meminta input kategori dari pengguna
- Memvalidasi jumlah uang (harus angka positif)
- Memvalidasi tanggal (format: YYYY-MM-DD)
- Menambahkan transaksi baru ke list
- Menambahkan kategori ke set

#### **`tampilan_per_kategori()`**

- **Menggunakan nested loop:**
  - Loop pertama: Iterasi melalui setiap kategori unik (dari set)
  - Loop kedua: Iterasi melalui list transaksi untuk mencocokkan kategori
  - Tampilkan transaksi yang sesuai kategori dengan format rapi

#### **`laporan_pengeluaran_boros()`**

- Menghitung total pengeluaran per kategori menggunakan dictionary
- Menggunakan kondisi if-else dengan operator logika
- Jika total kategori > Rp 1.000.000 → **Tampilkan Peringatan Boros**
- Menampilkan rekomendasi penghematan

#### **`validasi_input()`** (di utils)

- Memvalidasi input adalah angka
- Memvalidasi input tidak kosong
- Memvalidasi format tanggal

### 5.3 Listing Kode Python Lengkap

_Kode lengkap dapat dilihat di file-file berikut:_

- [main.py](main.py)
- [data/storage.py](data/storage.py)
- [services/tambah_transaksi.py](services/tambah_transaksi.py)
- [services/tampilan_per_kategori.py](services/tampilan_per_kategori.py)
- [services/laporan_transaksi.py](services/laporan_transaksi.py)
- [utils/validasi_input.py](utils/validasi_input.py)

---

## 6. UJI COBA & HASIL

### 6.1 Skenario Uji Coba

| No  | Skenario Uji                | Input                                                     | Output yang Diharapkan                             | Output Aktual | Status |
| --- | --------------------------- | --------------------------------------------------------- | -------------------------------------------------- | ------------- | ------ |
| 1   | Tambah transaksi valid      | Kategori: "Makanan", Jumlah: 50000, Tanggal: "2025-01-15" | Transaksi berhasil ditambahkan                     | ✓             | PASS   |
| 2   | Tambah dengan input negatif | Jumlah: -5000                                             | Error: "Jumlah harus positif"                      | ✓             | PASS   |
| 3   | Input kategori kosong       | Kategori: ""                                              | Error: "Kategori tidak boleh kosong"               | ✓             | PASS   |
| 4   | Tampilkan per kategori      | 5 transaksi, 3 kategori berbeda                           | Transaksi dikelompokkan per kategori (nested loop) | ✓             | PASS   |
| 5   | Deteksi pengeluaran boros   | Total "Makanan" = Rp 1.500.000                            | Peringatan: "Kategori Makanan melebihi batas!"     | ✓             | PASS   |
| 6   | Edit transaksi              | Ubah ID 1 dari 50000 menjadi 75000                        | Data transaksi ID 1 ter-update                     | ✓             | PASS   |
| 7   | Hapus transaksi             | Hapus transaksi ID 3                                      | Transaksi ID 3 dihapus dari list                   | ✓             | PASS   |
| 8   | Input tipe salah            | Input string untuk jumlah                                 | Error: "Input harus berupa angka"                  | ✓             | PASS   |

### 6.2 Screenshot Tampilan Program

_(Sisipkan screenshot dari eksekusi program)_

**Contoh Output:**

```
============ Aplikasi Manajemen Keuangan Harian =============

Menu:
 1. Tambah Transaksi
 2. Edit Transaksi
 3. Hapus Transaksi
 4. Tampilkan Semua Transaksi
 5. Tampilkan Transaksi per Kategori
 6. Deteksi Pengeluaran Boros
 7. Exit

Pilih Opsi: 1
```

### 6.3 Analisis Hasil Uji Coba

**Program sudah memenuhi semua persyaratan:**

- Input/Output berfungsi dengan baik
- If-else dan operator logika diterapkan untuk validasi
- Perulangan dan nested loop berfungsi dengan baik pada fitur "Tampilkan per Kategori"
- Fungsi modular telah dibuat lebih dari 2 fungsi
- Struktur data (list, set, dictionary) digunakan dengan efektif
- Validasi input mencegah error dan input tidak valid
- Program responsif dan user-friendly

**Kesimpulan:** Program berhasil diselesaikan dan telah memenuhi tujuan pembelajaran serta semua kriteria yang ditetapkan.

---

## 7. KESIMPULAN

### 7.1 Ringkasan Hasil Proyek

Aplikasi Manajemen Keuangan Harian berhasil dikembangkan dengan menggunakan Python. Aplikasi ini menyediakan fitur lengkap untuk membantu pengguna mencatat, mengelola, dan menganalisis pengeluaran harian mereka.

**Fitur Utama yang Berhasil Diimplementasikan:**

1. Tambah transaksi dengan validasi input
2. Edit dan hapus transaksi yang sudah tercatat
3. Tampilkan semua transaksi atau per kategori
4. Deteksi pengeluaran boros dengan peringatan otomatis
5. Interface menu yang user-friendly

### 7.2 Konsep Algoritma & Pemrograman yang Diterapkan

| Konsep                   | Penerapan                                   | File/Lokasi                  |
| ------------------------ | ------------------------------------------- | ---------------------------- |
| **Input/Output**         | Input dari pengguna dan output ke konsol    | main.py, semua services      |
| **Variabel & Tipe Data** | String, int, dict, list, set                | Semua file                   |
| **If-Else**              | Validasi input, kondisi menu, deteksi boros | Semua services               |
| **Operator Logika**      | AND, OR pada validasi kondisi               | utils/validasi_input.py      |
| **Loop (For)**           | Iterasi daftar transaksi                    | tampilan_transaksi.py        |
| **Loop (While)**         | Menu utama berjalan sampai exit             | main.py                      |
| **Nested Loop**          | Loop kategori + loop transaksi              | tampilan_per_kategori.py     |
| **Fungsi**               | 7+ fungsi buatan untuk modularitas          | services/\*, main.py         |
| **List**                 | Menyimpan daftar transaksi                  | data/storage.py              |
| **Set**                  | Menyimpan kategori unik                     | services/tambah_transaksi.py |
| **Dictionary**           | Menyimpan data transaksi                    | data/storage.py              |
| **Validasi Input**       | Error handling untuk input tidak valid      | utils/validasi_input.py      |

### 7.3 Kendala & Cara Mengatasinya

| Kendala                                     | Solusi                                               |
| ------------------------------------------- | ---------------------------------------------------- |
| **Data tidak persisten (hilang saat exit)** | Implementasi save/load dari file JSON atau database  |
| **Validasi tanggal kompleks**               | Menggunakan library `datetime` untuk parsing tanggal |
| **Input kategori case-sensitive**           | Normalisasi input (lowercase atau capitalize)        |
| **Performa dengan banyak data**             | Menggunakan dictionary untuk pencarian O(1)          |
| **Interface kurang menarik**                | Menambahkan warna dengan library `colorama`          |

### 7.4 Saran Pengembangan ke Depan

1. **Persistensi Data**

   - Simpan data ke file JSON atau SQLite database
   - Implementasi backup otomatis

2. **Fitur Tambahan**

   - Visualisasi grafik pengeluaran (matplotlib/plotly)
   - Filter transaksi berdasarkan rentang tanggal
   - Target budget per kategori
   - Export laporan ke PDF

3. **User Interface**

   - Migrasi ke GUI dengan Tkinter atau PyQt
   - Mode web dengan Flask/Django
   - Aplikasi mobile (Flutter/React Native)

4. **Analisis Data**

   - Prediksi pengeluaran menggunakan machine learning
   - Rekomendasi penghematan otomatis
   - Statistik pengeluaran bulanan/tahunan

5. **Keamanan**
   - Autentikasi pengguna
   - Enkripsi data sensitif
   - Logging aktivitas pengguna

---

## 8. DAFTAR PUSTAKA

### 8.1 Dokumentasi Resmi

1. **Python Software Foundation.** (2024). _Python 3 Documentation_.

   - Tersedia di: https://docs.python.org/3/
   - Referensi lengkap built-in functions, modules, dan best practices

2. **Python.org - Data Structures.** (2024).

   - Tersedia di: https://docs.python.org/3/tutorial/datastructures.html
   - Dokumentasi list, set, dan dictionary

3. **Python.org - Modules.** (2024).

   - Tersedia di: https://docs.python.org/3/reference/import.html
   - Referensi tentang import statements dan module system

4. **Python.org - Error Handling.** (2024).
   - Tersedia di: https://docs.python.org/3/tutorial/errors.html
   - Dokumentasi exception handling dan try-except blocks

### 8.2 Tutorial Online - W3Schools

1. **W3Schools.** _Python Tutorial_.

   - Link: https://www.w3schools.com/python/
   - Referensi cepat untuk sintaks dan konsep Python dasar

2. **W3Schools.** _Python User Input_.

   - Link: https://www.w3schools.com/python/python_user_input.asp
   - Tutorial tentang menerima input dari pengguna menggunakan `input()`

3. **W3Schools.** _Python For Loops_.

   - Link: https://www.w3schools.com/python/python_for_loops.asp
   - Panduan lengkap penggunaan for loops dalam Python

4. **W3Schools.** _Python While Loops_.

   - Link: https://www.w3schools.com/python/python_while_loops.asp
   - Tutorial about while loops dan kontrol loop

5. **W3Schools.** _Python Functions_.

   - Link: https://www.w3schools.com/python/python_functions.asp
   - Panduan membuat dan menggunakan fungsi dalam Python

6. **W3Schools.** _Python Modules_.

   - Link: https://www.w3schools.com/python/python_modules.asp
   - Tutorial tentang membuat dan menggunakan modules/modules

7. **W3Schools.** _Python String Formatting_.

   - Link: https://www.w3schools.com/python/python_string_formatting.asp
   - Panduan format string menggunakan f-strings dan format()

8. **W3Schools.** _Python Try Except_.
   - Link: https://www.w3schools.com/python/python_try_except.asp
   - Tutorial error handling dengan try-except blocks

### 8.3 Tutorial Online - Lainnya

1. **Python Wiki.** _For Loop_.

   - Link: https://wiki.python.org/moin/ForLoop
   - Penjelasan mendalam tentang for loops dan iterasi dalam Python

2. **Medium - Qemhal H.** _Different Ways to Display a Table in Python_.

   - Link: https://medium.com/@qemhal.h/different-ways-to-display-a-table-in-python-d867aefb624a
   - Panduan menampilkan data dalam format tabel yang rapi

3. **Real Python.** _Python f-strings: The Best String Formatting Option_.

   - Link: https://realpython.com/python-f-strings/
   - Panduan mendalam penggunaan f-strings untuk output yang rapi

---

**Dokumen ini dibuat sebagai bagian dari tugas Proyek Berbasis Pembelajaran (PBL) pada mata kuliah Algoritma & Pemrograman.**
