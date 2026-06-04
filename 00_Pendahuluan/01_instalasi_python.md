# Panduan Instalasi Python dan Pustaka Pendukung

Python adalah salah satu bahasa pemrograman utama yang digunakan dalam repositori ini untuk komputasi ilmiah dan simulasi fisika. Dokumen ini memandu Anda dalam melakukan instalasi Python, mengatur lingkungan virtual (*virtual environment*), serta memasang pustaka pendukung yang diperlukan.

---

## 1. Rekomendasi: Menggunakan Miniconda atau Anaconda

Untuk kebutuhan ilmiah, sangat disarankan menggunakan distribusi **Miniconda** (ringan) atau **Anaconda** (lengkap). Keduanya menyertakan manajer paket `conda` yang sangat andal dalam menangani dependensi pustaka C/C++ dan Fortran yang sering digunakan oleh pustaka Python ilmiah (seperti SciPy).

* **Miniconda (Disarankan):** Hanya berisi Python dan manajer paket `conda`. Unduh di: [Miniconda Download](https://docs.conda.io/en/latest/miniconda.html)
* **Anaconda:** Berisi Python, `conda`, dan ratusan pustaka ilmiah bawaan. Unduh di: [Anaconda Download](https://www.anaconda.com/download)

---

## 2. Pustaka Ilmiah yang Digunakan

Proyek ini memerlukan beberapa pustaka Python berikut yang didefinisikan dalam [environment.yml](file:///d:/My%20Project/physics/Physics_Dev/environment.yml) dan [requirements.txt](file:///d:/My%20Project/physics/Physics_Dev/requirements.txt):

* **NumPy ($\ge 1.22.0$):** Untuk komputasi array multi-dimensi dan fungsi matematika linier.
* **SciPy ($\ge 1.8.0$):** Menyediakan algoritma numerik tingkat lanjut (integrasi, optimasi, ODE, PDE).
* **Matplotlib ($\ge 3.5.0$):** Untuk visualisasi data dan pembuatan grafik 2D/3D.
* **Pandas ($\ge 1.4.0$):** Untuk analisis dan manipulasi data terstruktur.
* **Jupyter ($\ge 1.0.0$):** Antarmuka notebook interaktif untuk eksperimen kode.
* **Openpyxl ($\ge 3.0.0$):** Pustaka untuk membaca/menulis berkas Microsoft Excel (`.xlsx`).
* **Numba ($\ge 0.55.0$):** Compiler JIT (Just-In-Time) untuk mempercepat eksekusi fungsi Python mendekati kecepatan bahasa C.

---

## 3. Langkah-Langkah Instalasi Lingkungan Virtual

### Opsi A: Menggunakan Conda (Sangat Disarankan)
Setelah menginstal Miniconda/Anaconda, buka terminal atau *Anaconda Prompt* lalu jalankan perintah berikut di direktori utama repositori:

1. Buat lingkungan virtual bernama `physics` menggunakan berkas konfigurasi `environment.yml`:
   ```bash
   conda env create -f environment.yml
   ```
2. Aktifkan lingkungan virtual tersebut:
   ```bash
   conda activate physics
   ```

### Opsi B: Menggunakan Pip (Standard Python)
Jika Anda menggunakan Python standar (dari python.org) tanpa Conda:

1. Buat virtual environment di direktori proyek:
   ```bash
   python -m venv venv
   ```
2. Aktifkan virtual environment:
   * **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * **Windows (CMD):**
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   * **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
3. Pasang pustaka pendukung menggunakan berkas `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Verifikasi Instalasi

Untuk memastikan semua pustaka terpasang dengan benar dan siap digunakan, Anda dapat menjalankan skrip uji coba berikut. Simpan kode ini sebagai `test_env.py` atau jalankan langsung di terminal Python:

```python
import sys

print(f"Versi Python: {sys.version}")

try:
    import numpy as np
    print(f"NumPy: {np.__version__} - OK")
except ImportError:
    print("NumPy - BELUM TERPASANG")

try:
    import scipy
    print(f"SciPy: {scipy.__version__} - OK")
except ImportError:
    print("SciPy - BELUM TERPASANG")

try:
    import matplotlib
    print(f"Matplotlib: {matplotlib.__version__} - OK")
except ImportError:
    print("Matplotlib - BELUM TERPASANG")

try:
    import pandas as pd
    print(f"Pandas: {pd.__version__} - OK")
except ImportError:
    print("Pandas - BELUM TERPASANG")

try:
    import numba
    print(f"Numba: {numba.__version__} - OK")
except ImportError:
    print("Numba - BELUM TERPASANG")

print("\nVerifikasi selesai. Jika semua pustaka berstatus 'OK', lingkungan komputasi Anda siap!")
```

Jika ada pustaka yang belum terpasang, silakan ulangi langkah instalasi virtual environment di atas atau pasang secara manual dengan perintah `pip install [nama_pustaka]`.
