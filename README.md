# Physics

Repositori ini berisi implementasi komputasi fisika, metode numerik, dan alat bantu komputasi ilmiah dalam Python, MATLAB, dan Excel yang bersifat publik.

## Struktur Repositori
- `00_Pendahuluan/`: Panduan instalasi dan kontribusi.
- `01_Metode_Numerik/`: Algoritma matematika murni.
- `02_Fisika_Komputasi/`: Simulasi dan visualisasi kasus fisika.
- `03_Scientific_Computing/`: Alat bantu komputasi ilmiah, regresi data, dan paralelisme.
- `04_Proyek_Aplikasi/`: Aplikasi terintegrasi (simulasi dan visualisasi).
- `05_Topik_Advanced/`: Metode tingkat lanjut (FEM, LBM, MD, FDTD, PINNs).
- `06_Notebooks/`: Notebook demonstrasi interaktif.
- `07_Dataset/`: Dataset contoh dan hasil eksperimen.
- `08_Dokumentasi/`: Rujukan teoretis, panduan penamaan, dan roadmap proyek.

---

## Himbauan & Kontribusi Publik

Jika Anda menemukan adanya kesalahan penulisan rumus teori, penjelasan konsep fisika, ataupun kutipan baris kode program (*bug*), kami memohon maaf sebesar-besarnya. Kami sangat menghargai masukan dan partisipasi Anda untuk menyempurnakan proyek edukasi ini.

Sebagai repositori yang bersifat terbuka bagi pembelajaran, Anda dapat membantu berkontribusi memperbaiki teori atau kode melalui mekanisme resmi berikut:

### 1. Melaporkan Kesalahan Melalui GitHub Issues
Cara ini sangat direkomendasikan jika Anda menemukan kesalahan tetapi tidak ingin melakukan pengkodean/pengeditan berkas sendiri:
1. Masuk ke halaman repositori publik **`Physics`** di GitHub.
2. Klik tab **Issues** di bagian atas halaman.
3. Klik tombol **New Issue** (Buat Laporan Baru).
4. Berikan judul yang jelas (contoh: `Kesalahan Rumus di Metode Eliminasi Gauss`).
5. Pada bagian deskripsi, jelaskan secara detail:
   * Nama berkas dan baris keberapa kesalahan berada.
   * Kesalahan yang terjadi dan bagaimana seharusnya perbaikan yang benar (gunakan format rumus LaTeX jika diperlukan).
6. Klik **Submit new issue**. Laporan Anda akan ditinjau dan diperbaiki oleh pengembang utama.

### 2. Mengajukan Perbaikan Melalui Pull Request (PR)
Jika Anda ingin memperbaiki kesalahan teori atau kode program secara langsung:
1. Lakukan **Fork** pada repositori publik `Physics` ke akun GitHub pribadi Anda.
2. Clone repositori hasil fork tersebut ke komputer lokal Anda.
3. Buat cabang (*branch*) baru untuk pengerjaan perbaikan Anda:
   ```bash
   git checkout -b fix/deskripsi-perbaikan
   ```
4. Lakukan koreksi file, lalu lakukan commit perubahan dengan pesan yang deskriptif:
   ```bash
   git add .
   git commit -m "fix: memperbaiki penulisan rumus pada metode X"
   ```
5. Kirim (*push*) cabang perbaikan tersebut ke repositori fork Anda di GitHub:
   ```bash
   git push origin fix/deskripsi-perbaikan
   ```
6. Buka halaman repositori asli di GitHub, klik tombol **Compare & pull request**, lalu klik **Create pull request**. Kami akan memeriksa hasil perubahan Anda sebelum menggabungkannya (*merge*) ke cabang utama.

> [!NOTE]
> Panduan lebih detail mengenai standar penulisan kode, penamaan berkas, format docstrings, serta tata tertib kontribusi dapat dipelajari di berkas [05_panduan_kontribusi.md](file:///d:/My%20Project/physics/Physics/00_Pendahuluan/05_panduan_kontribusi.md).
