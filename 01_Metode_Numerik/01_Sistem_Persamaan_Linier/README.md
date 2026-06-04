# Modul 01.01: Sistem Persamaan Linier (SPL)

Sistem Persamaan Linier (SPL) adalah sekumpulan persamaan aljabar linier yang melibatkan variabel-variabel yang sama. Pemecahan SPL merupakan salah satu pilar utama dalam matematika komputasi dan fisika komputasi, karena hampir semua model fisika kontinu yang didiskritisasi (seperti metode beda hingga, elemen hingga, atau volume hingga) pada akhirnya akan bermuara pada penyelesaian SPL.

---

## 1. Definisi SPL dan Representasi Matriks

Secara matematis, sebuah sistem dengan $m$ persamaan linier dan $n$ variabel tidak diketahui dapat ditulis sebagai:

$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
\vdots \quad\quad\quad\quad\quad\quad\quad\quad\quad\quad &\quad \vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= b_m
\end{aligned}
$$

Dalam notasi aljabar matriks, sistem di atas dapat direpresentasikan secara ringkas sebagai:

$$Ax = b$$

Di mana:
* $A$ adalah matriks koefisien berukuran $m \times n$.
* $x$ adalah vektor kolom variabel berukuran $n \times 1$.
* $b$ adalah vektor kolom konstanta berukuran $m \times 1$.

Dalam modul ini, kita akan fokus pada kasus di mana $m = n$ (jumlah persamaan sama dengan jumlah variabel) dan matriks $A$ memiliki invers ($A^{-1}$ ada), sehingga sistem memiliki solusi unik yang diberikan secara formal oleh $x = A^{-1}b$.

---

## 2. Mengapa Menggunakan Metode Numerik?

Secara teoritis (analitik), kita dapat memecahkan SPL menggunakan:
1. **Aturan Cramer:** Memerlukan perhitungan determinan matriks.
2. **Invers Matriks Langsung ($A^{-1}$):** Menghitung matriks adjoin dibagi determinan.

Namun, untuk implementasi komputer praktis, metode analitik ini sangat tidak efisien dan seringkali gagal karena alasan berikut:

* **Kompleksitas Komputasi ($O(N!)$ atau $O(N^3)$):** Menghitung determinan dengan Aturan Cramer untuk matriks berukuran besar memiliki kompleksitas $O(N!)$ yang mustahil dijalankan komputer bahkan untuk $N=20$. Perhitungan invers langsung memiliki kompleksitas $O(N^3)$ yang sangat lambat untuk matriks besar.
* **Kestabilan Numerik & Round-off Error:** Representasi angka pecahan (*floating-point*) pada komputer memiliki presisi terbatas. Melakukan operasi matriks analitik secara langsung dapat mengakibatkan penumpukan kesalahan pembulatan (*round-off error*) yang besar, terutama pada matriks yang **ill-conditioned** (matriks di mana perubahan sangat kecil pada $b$ menyebabkan perubahan sangat besar pada $solusi\ x$).
* **Matriks Jarang (*Sparse Matrices*):** Dalam simulasi fisika nyata (seperti simulasi aliran fluida atau perpindahan panas), matriks koefisien $A$ sering kali berupa matriks raksasa (misal $10^6 \times 10^6$) di mana $99\%$ elemennya bernilai nol. Metode numerik iteratif (seperti Jacobi atau Gauss-Seidel) dapat mengeksploitasi struktur ini untuk menghemat memori dan waktu komputasi secara signifikan.

---

## 3. Contoh Penerapan SPL dalam Fisika dan Teknik

* **Analisis Rangkaian Listrik (Hukum Kirchhoff):**
  Dalam rangkaian listrik multi-loop, penerapan Hukum Arus Kirchhoff (KCL) dan Hukum Tegangan Kirchhoff (KVL) menghasilkan sistem persamaan linier di mana variabel yang dicari adalah arus loop ($I_i$) atau tegangan simpul ($V_i$).
  
* **Analisis Struktur Truss (Mekanika Teknik):**
  Untuk menentukan gaya-gaya internal yang bekerja pada rangka jembatan atau gedung, para insinyur menyusun persamaan kesetimbangan gaya ($\Sigma F_x = 0$ dan $\Sigma F_y = 0$) pada setiap titik sambung (*joint*), yang membentuk SPL berukuran besar.
  
* **Persamaan Distribusi Panas (Beda Hingga):**
  Untuk menghitung temperatur pada suatu logam secara numerik, persamaan diferensial parsial distribusi panas (persamaan Laplace/Poisson) didiskritisasi menggunakan metode beda hingga. Temperatur di setiap titik kisi grid dihubungkan dengan temperatur titik-titik tetangganya, membentuk sistem persamaan linier besar $Ax = b$.
  
* **Jaringan Pegas-Massa Terhubung:**
  Sistem dinamik yang terdiri dari banyak pegas dan massa yang terhubung satu sama lain dalam keadaan setimbang statis dapat dimodelkan sebagai sistem persamaan linier untuk menentukan simpangan masing-masing massa.

---

## Daftar Metode yang Tersedia

Berikut adalah metode-metode numerik penyelesaian SPL yang diimplementasikan dalam repositori ini:

1. **[01. Eliminasi Gauss](file:///d:/My%20Project/physics/Physics_Dev/01_Metode_Numerik/01_Sistem_Persamaan_Linier/01_eliminasi_gauss.md)** - Metode langsung dengan eliminasi maju dan substitusi mundur.
2. **02. Eliminasi Gauss-Jordan** - Variasi Eliminasi Gauss untuk mengubah matriks menjadi matriks identitas.
3. **03. Dekomposisi LU** - Memfaktorkan matriks $A$ menjadi matriks segitiga bawah ($L$) dan segitiga atas ($U$).
4. **04. Dekomposisi Cholesky** - Dekomposisi khusus untuk matriks simetris positif definit.
5. **05. Iterasi Jacobi** - Metode iteratif dasar.
6. **06. Iterasi Gauss-Seidel** - Metode iteratif yang lebih cepat konvergen dibanding Jacobi.
7. **07. Successive Over-Relaxation (SOR)** - Akselerasi konvergensi Gauss-Seidel dengan parameter relaksasi.
8. **08. Conjugate Gradient (CG)** - Metode iteratif untuk matriks simetris positif definit berukuran besar.
9. **09. Generalized Minimal Residual (GMRES)** - Metode iteratif proyeksi Krylov untuk matriks non-simetris.
10. **10. BiConjugate Gradient (BiCG)** - Alternatif CG untuk matriks non-simetris.
11. **11. Dekomposisi QR** - Faktorisasi matriks menggunakan matriks ortogonal ($Q$) dan matriks segitiga atas ($R$).
12. **12. Pseudoinverse & SVD** - Penyelesaian SPL untuk kasus matriks singular atau non-persegi (*overdetermined/underdetermined*).
