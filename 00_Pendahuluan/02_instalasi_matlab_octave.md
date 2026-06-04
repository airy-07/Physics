# Panduan Instalasi MATLAB & GNU Octave

Selain Python, repositori ini juga menyediakan implementasi numerik menggunakan **MATLAB** dan **GNU Octave**. MATLAB merupakan standar industri dan akademik untuk komputasi teknis, sedangkan GNU Octave adalah alternatif gratis dan *open-source* yang memiliki kompatibilitas sintaksis sangat tinggi dengan MATLAB.

---

## 1. MATLAB (Komersial / Lisensi Akademik)

Jika Anda memiliki akses ke lisensi MATLAB (baik melalui kampus, kantor, atau personal):
1. Unduh penginstal dari situs resmi [MathWorks](https://www.mathworks.com/).
2. Pasang MATLAB beserta *toolboxes* dasar berikut (opsional, namun direkomendasikan):
   * **Symbolic Math Toolbox:** Berguna untuk penyelesaian persamaan simbolik (misal dalam fisika teori).
   * **Control System Toolbox:** Berguna untuk analisis sistem dinamik dan kontrol.
   * **Optimization Toolbox:** Berguna untuk pencarian nilai minimum/maksimum fungsi multi-variabel.

---

## 2. GNU Octave (Gratis & Open-Source)

Jika Anda tidak memiliki lisensi MATLAB, GNU Octave adalah pilihan yang sangat baik karena sebagian besar kode MATLAB (`.m`) dalam repositori ini dapat langsung dijalankan di Octave tanpa modifikasi.

### Cara Instalasi GNU Octave:

* **Windows:**
  1. Unduh installer `.exe` terbaru dari [GNU Octave Windows Download](https://www.gnu.org/software/octave/download).
  2. Jalankan installer dan ikuti petunjuk pemasangan hingga selesai.
  3. Buka pintasan *Octave (GUI)* untuk menggunakan antarmuka grafis.

* **macOS:**
  Instalasi paling mudah dilakukan menggunakan manajer paket **Homebrew**:
  ```bash
  brew install octave
  ```

* **Linux (Debian/Ubuntu):**
  Jalankan perintah berikut di terminal:
  ```bash
  sudo apt-get update
  sudo apt-get install octave
  ```

---

## 3. Instalasi Paket Tambahan (*Packages*) di GNU Octave

Beberapa fungsionalitas matematika tingkat lanjut memerlukan paket tambahan yang setara dengan *toolbox* MATLAB. Paket ini dapat dipasang secara langsung dari repositori *Octave Forge*.

Buka GUI Octave atau terminal Octave, lalu jalankan perintah berikut:

1. **Paket Symbolic** (diperlukan untuk matematika simbolik):
   ```octave
   pkg install -forge symbolic
   ```
   *(Catatan untuk pengguna Windows: paket symbolic memerlukan Python dan pustaka SymPy terpasang di sistem).*
   
2. **Paket Control** (diperlukan untuk sistem kendali):
   ```octave
   pkg install -forge control
   ```

Setiap kali Anda ingin menggunakan fungsionalitas dari paket tersebut di dalam skrip Octave, pastikan Anda memuat paket tersebut terlebih dahulu di awal baris skrip menggunakan perintah:
```octave
pkg load symbolic
pkg load control
```

---

## 4. Verifikasi Instalasi

Untuk memastikan MATLAB atau GNU Octave Anda berfungsi dengan baik, jalankan perintah atau skrip uji coba sederhana berikut di *Command Window*:

```octave
% 1. Uji Operasi Matriks Dasar
A = [1, 2; 3, 4];
B = [5, 6; 7, 8];
C = A * B;

disp("Hasil Perkalian Matriks C = A * B:");
disp(C);

% 2. Uji Plot Sederhana
x = linspace(0, 2*pi, 100);
y = sin(x);
plot(x, y, 'r-', 'LineWidth', 2);
title('Verifikasi Plot MATLAB/Octave');
xlabel('x');
ylabel('sin(x)');
grid on;

disp("Jika matriks tercetak dan jendela grafik plot sinus muncul, instalasi Anda sukses!");
```

Jika terjadi error saat menjalankan plot di Octave Linux, pastikan pustaka grafik terinstal dengan menjalankan perintah `sudo apt install gnuplot` di terminal sistem Anda.
