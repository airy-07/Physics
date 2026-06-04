# Penjelasan Struktur Repositori

Repositori ini memiliki tata letak yang sangat terstruktur untuk memudahkan navigasi, pembelajaran, pengembangan, serta portabilitas kode di antara beberapa bahasa pemrograman dan perkakas (Python, MATLAB, dan Excel). 

Berikut adalah peta struktur folder dan panduan tata kelola repositori ini.

---

## 1. Peta Folder Utama

Repositori ini dibagi menjadi 9 modul utama (diindeks dari `00` sampai `08`), masing-masing memiliki fokus pembelajaran dan aplikasi yang spesifik:

* **`00_Pendahuluan/`**: Berisi dokumen persiapan awal, panduan instalasi perangkat lunak (Python, MATLAB/Octave, Jupyter), penjelasan struktur repositori, dan panduan kontribusi.
* **`01_Metode_Numerik/`**: Implementasi algoritma matematika dasar tanpa konteks fisika spesifik. Terdiri dari subfolder seperti sistem persamaan linier, akar persamaan, interpolasi, diferensiasi, integrasi, serta persamaan diferensial biasa (ODE) dan parsial (PDE).
* **`02_Fisika_Komputasi/`**: Penerapan metode numerik pada domain fisika spesifik seperti Mekanika Klasik, Elektromagnetisme, Fisika Fluida, Termodinamika, Mekanika Kuantum, Astrofisika, Fisika Lingkungan, dan Relativitas.
* **`03_Scientific_Computing/`**: Topik rekayasa komputasi ilmiah seperti visualisasi data lanjut, regresi & pencocokan kurva (*fitting*), analisis ketidakpastian/error, pemrograman paralel/akselerasi kode (Numba, CuPy), dan manajemen data (membaca/menulis CSV, Excel, JSON).
* **`04_Proyek_Aplikasi/`**: Aplikasi simulasi skala menengah yang mandiri (*standalone*) dan interaktif, lengkap dengan grafik dan penyimpanan hasil simulasi (misalnya simulasi tata surya, distribusi suhu pelat, atau model Ising).
* **`05_Topik_Advanced/`**: Metode komputasi tingkat lanjut yang digunakan dalam riset dan industri seperti FDM, FEM, FVM, Lattice Boltzmann Method (LBM), Dinamika Molekuler (MD), FDTD Elektromagnetik, dan Machine Learning untuk Fisika (seperti PINN - *Physics-Informed Neural Networks*).
* **`06_Notebooks/`**: Kumpulan dokumen Jupyter Notebook (`.ipynb`) interaktif yang menggabungkan visualisasi dan penjelasan teori singkat untuk demo cepat.
* **`07_Dataset/`**: Berkas data mentah (`.csv`) yang digunakan sebagai bahan masukan (*input*) untuk simulasi fisika atau latihan analisis data ilmiah.
* **`08_Dokumentasi/`**: Dokumen referensi, daftar buku/paper referensi, daftar rumus fisika, aturan penamaan berkas yang detail, dan rencana pengembangan (*roadmap*).

---

## 2. Struktur Organisasi Internal Folder

Untuk memastikan konsistensi, setiap sub-topik di bawah modul `01` dan `02` diorganisasikan berdasarkan teknologi atau bahasa pemrograman yang digunakan:

```text
[Nama_Topik]/
├── Excel/
│   └── [nomor]_[nama_metode].xlsx
├── MATLAB/
│   └── [nomor]_[nama_metode].m
└── Python/
    └── [nomor]_[nama_metode].py
```

* **`Excel/`**: Menyimpan lembar kerja Microsoft Excel (`.xlsx`) untuk visualisasi perhitungan numerik sel demi sel (sangat berguna untuk memahami langkah iteratif secara visual).
* **`MATLAB/`**: Menyimpan berkas kode MATLAB/Octave (`.m`).
* **`Python/`**: Menyimpan berkas kode Python (`.py`).

---

## 3. Berkas-Berkas Penting di Root Direktori

Di direktori utama repositori, terdapat berkas-berkas konfigurasi dan pelacakan berikut:

* **[environment.yml](file:///d:/My%20Project/physics/Physics_Dev/environment.yml)**: Berkas konfigurasi untuk membuat *virtual environment* menggunakan Conda.
* **[requirements.txt](file:///d:/My%20Project/physics/Physics_Dev/requirements.txt)**: Berkas daftar pustaka Python untuk instalasi menggunakan `pip`.
* **[PROGRES.md](file:///d:/My%20Project/physics/Physics_Dev/PROGRES.md)**: Lembar pemantauan status pengerjaan, revisi, dan sinkronisasi berkas dari repositori pengembangan privat (`Physics_Dev`) ke repositori publik (`Physics`).
* **`auto_logbook.py`**: Skrip Python otomatis yang mendeteksi perubahan berkas dan memperbarui log aktivitas pengkodean (*logbook*) secara berkala.

---

## 4. Konvensi Penamaan Berkas

Agar struktur repositori tetap rapi dan seragam, seluruh kontributor wajib mengikuti aturan penamaan berkas berikut:
1. Gunakan huruf kecil semua (*lowercase*).
2. Gunakan garis bawah (*underscore*) sebagai pemisah kata, hindari spasi (format `snake_case`).
3. Berikan nomor urut dua digit di depan nama file (contoh: `01_eliminasi_gauss.py`, `02_metode_regula_falsi.py`) untuk menjaga urutan logis pengerjaan materi.
4. Hindari nama berkas yang ambigu atau terlalu pendek (gunakan `05_iterasi_jacobi.py` daripada `jacobi.py`).
5. Kode di dalam folder `MATLAB/` dan `Python/` harus memiliki fungsionalitas yang identik untuk algoritma yang sama guna mempermudah perbandingan silang (*cross-comparison*).
