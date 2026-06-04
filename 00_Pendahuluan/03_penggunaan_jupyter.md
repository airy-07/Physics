# Panduan Penggunaan Jupyter Notebook & JupyterLab

Jupyter Notebook dan JupyterLab adalah lingkungan pengembangan interaktif berbasis web yang sangat populer di kalangan ilmuwan dan peneliti. Jupyter memungkinkan Anda menggabungkan kode eksekusi (Python/Julia/R), teks penjelasan formatted (Markdown), rumus matematika (LaTeX), serta visualisasi grafik langsung dalam satu dokumen tunggal (`.ipynb`).

---

## 1. Menjalankan Jupyter

Pastikan virtual environment Anda telah aktif sebelum menjalankan perintah berikut. Buka terminal atau Command Prompt di direktori proyek Anda, lalu jalankan salah satu dari perintah ini:

* **Jupyter Notebook (Versi Klasik):**
  ```bash
  jupyter notebook
  ```
* **JupyterLab (Antarmuka Modern Multi-Tab - Disarankan):**
  ```bash
  jupyter lab
  ```

Setelah menjalankan perintah tersebut, server lokal akan berjalan di latar belakang, dan peramban web (*browser*) Anda akan otomatis terbuka mengarah ke alamat `http://localhost:8888`.

---

## 2. Mengenal Sel (*Cells*)

Di Jupyter, dokumen terbagi menjadi sel-sel terpisah. Ada dua jenis sel utama yang paling sering digunakan:

1. **Sel Kode (Code Cell):** Digunakan untuk menulis dan mengeksekusi kode Python. Hasil output (teks maupun grafik) akan langsung ditampilkan di bawah sel tersebut setelah dieksekusi.
2. **Sel Teks (Markdown Cell):** Digunakan untuk menulis dokumentasi. Mendukung format teks tebal, miring, daftar poin, tautan, gambar, serta penulisan rumus fisika berbasis LaTeX. Contoh rumus LaTeX di dalam Markdown:
   * Rumus inline: `$E = mc^2$` akan menampilkan $E = mc^2$.
   * Rumus blok/display: `$$i\hbar\frac{\partial}{\partial t}\Psi = \hat{H}\Psi$$` akan menampilkan persamaan Schrödinger secara rapi di tengah halaman.

---

## 3. Pintasan Keyboard (*Keyboard Shortcuts*) Penting

Jupyter memiliki dua mode interaksi: **Mode Edit** (sel berwarna hijau/biru dengan kursor aktif) dan **Mode Perintah** (sel berbingkai abu-abu/biru tanpa kursor aktif).

Tekan `Esc` untuk masuk ke Mode Perintah, dan tekan `Enter` untuk masuk ke Mode Edit pada sel terpilih.

### Pintasan saat berada di Mode Perintah (setelah menekan `Esc`):
* **`A`**: Membuat sel baru di **atas** (*above*) sel aktif.
* **`B`**: Membuat sel baru di **bawah** (*below*) sel aktif.
* **`D` lalu `D`** (tekan D dua kali): Menghapus sel yang aktif.
* **`M`**: Mengubah tipe sel menjadi **Markdown** (sel teks).
* **`Y`**: Mengubah tipe sel menjadi **Code** (sel kode).
* **`Up / Down Arrow`**: Berpindah antar sel.

### Pintasan Umum untuk Eksekusi Kode:
* **`Shift + Enter`**: Mengeksekusi sel aktif dan berpindah ke sel di bawahnya.
* **`Ctrl + Enter`**: Mengeksekusi sel aktif tanpa berpindah tempat.
* **`Alt + Enter`**: Mengeksekusi sel aktif dan membuat sel baru tepat di bawahnya.

---

## 4. Perintah *Magic* (*Jupyter Magic Commands*)

Jupyter menyediakan perintah khusus (*magic commands*) untuk membantu pengujian dan optimasi performa kode. Perintah ini diawali dengan karakter `%` (untuk satu baris) atau `%%` (untuk seluruh isi sel).

Berikut adalah beberapa yang sangat berguna untuk fisika komputasi:

* **`%matplotlib inline`**: Menghasilkan grafik plot Matplotlib statis langsung di dalam notebook.
* **`%matplotlib widget`**: Membuat grafik Matplotlib menjadi interaktif (bisa di-zoom, digeser, dan disimpan). Memerlukan paket `ipympl`.
* **`%time [perintah]`**: Mengukur waktu eksekusi dari satu baris perintah tertentu.
* **`%timeit [perintah]`**: Mengukur waktu eksekusi baris perintah secara akurat dengan menjalankannya berulang kali (sangat berguna untuk benchmark kecepatan fungsi numerik).
* **`%%time`** (diletakkan di baris paling atas sel): Mengukur total waktu eksekusi untuk seluruh kode yang ada di dalam sel tersebut.

---

## 5. Menyimpan dan Menutup dengan Aman

* **Menyimpan:** Tekan `Ctrl + S` atau klik ikon disket di kiri atas.
* **Menghentikan Kernel:** Jika ada simulasi yang terjebak dalam *infinite loop* (perulangan tak terbatas), Anda dapat menghentikannya dengan menekan tombol **Interrupt** (ikon kotak hitam / stop) di toolbar atas.
* **Menutup Dokumen:** Jangan langsung menutup tab browser. Klik menu `File` -> `Close and Shutdown Notebook` (di JupyterLab) atau klik `File` -> `Close and Halt` (di Jupyter Classic) agar penggunaan memori RAM komputer Anda dilepaskan kembali secara bersih.
