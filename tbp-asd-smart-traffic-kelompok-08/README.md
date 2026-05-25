## KELOMPOK-8-Smart-Traffic-Signal-Optimalization

topik 7 Smart Traffic Simulation & Signal Optimalization

## Team

1.   **Alwan Fadhilah Rafianza**_25051030077
2.   **Arwan Adrean**_25051030065
3.   **Faqih Rizky Saputra**_25051030048
4.   **Amanda Lulu Prasetia**_25051030079


---

## Mata Kuliah

Algoritma dan Struktur Data
S1 Teknik Elektro
Universitas Negeri Yogyakarta

---

## Deskripsi Project

Project Smart Traffic Simulation & Signal Optimization adalah simulasi sistem lalu lintas kota berbasis CLI yang menggunakan struktur data dan algoritma seperti Graph, Priority Queue, BST, DFS, dan Dijkstra untuk mengatur arus kendaraan, menentukan prioritas kendaraan darurat, mencari rute tercepat, serta menganalisis kemacetan pada jaringan jalan kota secara efisien.

---

## Struktur Data yang Digunakan

Struktur data yang digunakan pada project Smart Traffic Simulation & Signal Optimization, yaitu:

* Graph (Graf)

  - Digunakan untuk merepresentasikan jaringan jalan dan persimpangan kota.

* Priority Queue

  - Digunakan untuk mengatur prioritas kendaraan, di mana ambulans diproses lebih dahulu.

* Stack

  - Digunakan untuk menyimpan riwayat atau siklus lampu lalu lintas.

* Binary Search Tree (BST)

  - Digunakan untuk pencarian cepat data persimpangan berdasarkan nama.

## Fitur Program

Fitur utama pada program Smart Traffic Simulation & Signal Optimization, yaitu:

* Manajemen Jaringan Jalan
* Pengelolaan Antrian Kendaraan
* Pencarian Rute Tercepat
* Pengelolaan Data Persimpangan
* Analisis dan Laporan Kemacetan
* Command Line Interface (CLI) Simulasi

---

## Instalasi

1. Clone atau download repository ini.
2. Buka terminal pada folder proyek.
3. Install dependensi yang diperlukan:

```bash
pip install -r requirements.txt
```

---

## Cara Menjalankan Program

Jalankan file utama:

```bash
python main.py
```

Setelah program berjalan, terminal akan menampilkan menu CLI dan pengguna dapat memasukkan perintah yang tersedia.

---

## Struktur Folder

```tbp
tbp-asd-kelompok-08/
│
├── AI_Log/                  # Menyimpan log atau catatan proses pengerjaan project
│
├── screenshots/             # Berisi screenshot output program dan dokumentasi sistem
│
├── docs/                    # Berisi laporan akhir dan slide presentasi project
│
├── experiments/             # Digunakan untuk benchmark dan pengujian performa algoritma
│
├── src/                     # Folder utama source code program
│   │
│   ├── data_structures/     # Implementasi struktur data seperti Graph, Queue, BST, Stack
│   │
│   ├── modules/             # Berisi modul fitur sistem simulasi lalu lintas
│   │
│   └── main.py              # Program utama untuk menjalankan sistem CLI
│
├── tests/                   # Berisi file pengujian sistem dan struktur data
│
├── .gitignore               # File yang diabaikan saat upload ke GitHub
│
├── requirements.txt         # Daftar library Python yang dibutuhkan
│
└── README.md                # Dokumentasi utama project dan cara menjalankan program
```
