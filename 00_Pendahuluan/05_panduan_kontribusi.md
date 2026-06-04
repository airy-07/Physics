# Panduan Kontribusi

Untuk menjaga kerapian, kegunaan, dan keandalan kode simulasi fisika komputasi di repositori ini, semua kontributor diharapkan mengikuti aturan dan alur kerja kolaboratif yang dijelaskan di bawah ini.

---

## 1. Alur Kerja Git & Sinkronisasi Repositori

Pengembangan kode dilakukan secara eksklusif di repositori pengembangan privat (**`Physics_Dev`**). Setelah kode diuji dan siap dirilis ke publik, kode disinkronkan ke repositori publik (**`Physics`**).

### A. Alur Kerja Fitur Baru atau Perbaikan:
1. Pastikan Anda berada di cabang (*branch*) `main` yang bersih dan mutakhir:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Buat cabang baru untuk pengerjaan fitur/perbaikan tertentu:
   ```bash
   git checkout -b feature/nama-fitur-anda
   ```
3. Lakukan pengkodean, lalu simpan perubahan Anda dengan commit yang deskriptif:
   ```bash
   git add .
   git commit -m "feat: menambah metode Runge-Kutta Orde 4 di Python"
   ```
4. Kirim cabang ke repositori privat (`Physics_Dev`):
   ```bash
   git push origin feature/nama-fitur-anda
   ```
5. Buat *Pull Request* (PR) di GitHub ke cabang `main` repositori privat untuk ditinjau (*code review*).

---

## 2. Pelacakan Progres via `PROGRES.md`

Setiap kali Anda mulai mengerjakan, merevisi, atau merilis berkas baru, Anda wajib memperbarui statusnya di berkas [PROGRES.md](file:///d:/My%20Project/physics/Physics_Dev/PROGRES.md) dengan panduan sebagai berikut:

* **`[ ]` (Belum Dikerjakan):** Berkas masih berupa berkas kosong atau boilerplate, dan belum diimplementasikan di repositori privat maupun publik.
* **`[~]` (Sedang Direvisi / Belum Sinkron):** Berkas sudah dikerjakan/direvisi di repositori privat (`Physics_Dev`), tetapi perubahannya belum dipublikasikan ke repositori publik (`Physics`).
* **`[x]` (Selesai & Sinkron):** Berkas sudah selesai diuji di repositori privat, dan isinya telah disinkronkan sepenuhnya ke repositori publik.

### Cara Memeriksa Perbedaan Antara Repositori Privat dan Publik:
Gunakan perintah Git berikut untuk melihat daftar berkas yang sudah dimodifikasi di privat tetapi belum dipublikasikan:
```bash
git fetch public
git diff public/main --name-only
```

---

## 3. Aturan Gaya Penulisan Kode (*Code Style*)

### Python (Mengacu pada PEP 8)
* **Penamaan:**
  * Gunakan `snake_case` untuk nama fungsi dan variabel (contoh: `hitung_energi_kinetik(m, v)`).
  * Gunakan `PascalCase` untuk nama kelas (contoh: `SimulasiPendulum`).
  * Gunakan huruf kapital semua untuk konstanta fisika (contoh: `GRAVITASI_G = 9.80665`).
* **Indentasi:** Gunakan 4 spasi (jangan gunakan tab).
* **Dokumentasi (Docstrings):** Setiap fungsi wajib memiliki deskripsi singkat mengenai parameter masukan (*input*) dan keluaran (*output*), tipe datanya, serta persamaan fisika yang diimplementasikan.

### MATLAB / Octave
* **Penamaan:**
  * Gunakan `camelCase` atau `snake_case` secara konsisten untuk variabel.
  * Gunakan nama berkas `.m` yang sama persis dengan nama fungsi utama di dalamnya.
* **Komentar:** Berikan penjelasan langkah-langkah logika komputasi pada blok kode yang kompleks agar mudah dibaca oleh kontributor lain.

### Markdown & Penulisan Rumus Fisika
* Jelaskan teori fisika secara singkat di awal dokumen/skrip.
* Tulis persamaan matematika menggunakan format LaTeX standar dengan pembatas `$` (inline) atau `$$` (blok/display) agar dapat dirender dengan baik di GitHub Markdown.

---

## 4. Format Pesan Commit (*Commit Message Convention*)

Gunakan format pesan commit yang terstandarisasi untuk mempermudah pelacakan riwayat perubahan:

* **`feat: ...`** -> Menambah fitur atau metode baru (contoh: `feat: tambah metode simpson 1/3 di python`).
* **`fix: ...`** -> Memperbaiki bug atau kesalahan logika kode (contoh: `fix: perbaiki pembagian dengan nol pada metode secant`).
* **`docs: ...`** -> Memperbarui dokumentasi atau file markdown (contoh: `docs: perbarui panduan instalasi python`).
* **`refactor: ...`** -> Merestrukturisasi kode tanpa mengubah fungsionalitasnya (contoh: `refactor: optimasi array slicing pada persamaan panas`).
