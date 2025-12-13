<h2 style="color: #f5f5f5f; font-weight: bold; background: #0096c7; padding: 1rem; border-radius: 1rem;">Aplikasi Manajemen Keuangan Harian</h2>

<p style="padding: 12px;text-decoration: underline; font-size: 16px;">Program mencatat Pengeluaran:</p>

- Data transaksi: kategori, jumlah, tanggal.
- Disimpan ke list of dictionary.
- Kategori unik disimpan ke set.
- Fitur:
  - Tambah transaksi.
  - Tampilkan transaksi per kategori (nested loop).
  - Hitung total per kategori (fungsi).
  - Deteksi pengeluaran boros:
    - Jika total kategori > 1.000.000 → tampilkan peringatan.

#### Struktur Project

<br/>finance_manager/
<br/>│ │
<br/>│ ├── main.py
<br/>│ │
<br/>│ ├── data/
<br/>│ │ └── storage.py
<br/>│ │
<br/>│ ├── services/
<br/>│ │ ├── transaction_service.py
<br/>│ │ └── analytics_service.py
<br/>│ │
<br/>│ └── utils/
<br/>│ ├── validator.py
<br/>│ ├── formatter.py
<br/>│ └── display.py
<br/>│
<br/>└── README.md

- main.py : file utama buat eksekusi dan tempat penaruhan modul
- data/ : tempat menyimpan data-data seperti list, tupple, dll
- services/ : tempat untuk file yang menyimpan logic
- utils/ : tempan untuk menyimpan sebuah fungsi modul kecil pembantu, seperti tampilan(UI)
