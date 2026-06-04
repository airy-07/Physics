# Catatan Metode: Eliminasi Gauss

Eliminasi Gauss adalah salah satu metode numerik langsung (*direct method*) yang paling fundamental untuk menyelesaikan Sistem Persamaan Linier (SPL) berbentuk:

$$Ax = b$$

Metode ini bekerja dengan melakukan serangkaian **Operasi Baris Elementer (OBE)** pada matriks diperbesar (*augmented matrix*) $[A | b]$ untuk mengubahnya menjadi matriks segitiga atas (*upper triangular matrix*). Setelah matriks segitiga atas terbentuk, nilai variabel dicari dengan metode substitusi mundur (*back substitution*).

---

## 1. Algoritma dan Langkah Numerik

Proses Eliminasi Gauss terbagi menjadi dua tahap utama:

### Tahap 1: Eliminasi Maju (*Forward Elimination*)
Tujuan tahap ini adalah menghilangkan elemen-elemen di bawah diagonal utama matriks $A$.
Untuk kolom $k = 1, 2, \dots, n-1$:
1. Tentukan elemen pivot $a_{kk}$.
2. Untuk setiap baris di bawahnya, yaitu baris $i = k+1, k+2, \dots, n$:
   * Hitung faktor pengali:
     $$m_{ik} = \frac{a_{ik}}{a_{kk}}$$
   * Lakukan OBE pada elemen matriks $A$ dan vektor $b$:
     $$a_{ij} \leftarrow a_{ij} - m_{ik} a_{kj} \quad \text{untuk } j = k, k+1, \dots, n$$
     $$b_i \leftarrow b_i - m_{ik} b_k$$

Di akhir tahap ini, sistem berubah bentuk menjadi:

$$
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
0 & a_{22}' & \dots & a_{2n}' \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & a_{nn}^{(n-1)}
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ \vdots \\ x_n
\end{bmatrix}
=
\begin{bmatrix}
b_1 \\ b_2' \\ \vdots \\ b_n^{(n-1)}
\end{bmatrix}
$$

### Tahap 2: Substitusi Mundur (*Back Substitution*)
Setelah matriks koefisien berbentuk segitiga atas, kita menghitung solusi variabel $x$ dari baris paling bawah naik ke atas:
1. Hitung variabel terakhir:
   $$x_n = \frac{b_n^{(n-1)}}{a_{nn}^{(n-1)}}$$
2. Hitung variabel lainnya untuk $i = n-1, n-2, \dots, 1$:
   $$x_i = \frac{b_i - \sum_{j=i+1}^n a_{ij} x_j}{a_{ii}}$$

---

## 2. Pentingnya *Partial Pivoting* (Tata-Utama Sebagian)

Dalam komputer, pembagian dengan angka yang sangat kecil atau nol dapat menyebabkan bencana numerik:
* **Pembagian dengan Nol:** Jika $a_{kk} = 0$, perhitungan faktor pengali $m_{ik} = a_{ik}/a_{kk}$ menghasilkan nilai tak hingga (*NaN/Inf*).
* **Round-off Error Ekstrim:** Jika $a_{kk}$ sangat kecil (misal $10^{-16}$), pembagian $a_{ik}/a_{kk}$ akan menghasilkan angka yang sangat besar. Ketika angka besar ini dikurangkan dari baris lain, informasi numerik yang kecil pada baris tersebut akan hilang akibat batas presisi *floating-point* komputer (efek *loss of significance*).

**Solusi: Partial Pivoting**
Sebelum mengeliminasi kolom $k$, kita mencari baris $p$ di bawah diagonal (dari baris $k$ hingga $n$) yang memiliki nilai mutlak elemen terbesar pada kolom tersebut:
$$\text{Cari } p \ge k \text{ sedemikian hingga } |a_{pk}| = \max_{j=k}^n |a_{jk}|$$

Jika $p \neq k$, kita menukar baris $k$ dengan baris $p$ (baik pada matriks $A$ maupun vektor $b$). Teknik ini memastikan pembagi $a_{kk}$ selalu bernilai sebesar mungkin, menjaga kestabilan numerik secara optimal.

---

## 3. Contoh Perhitungan Manual (Sederhana)

Selesaikan sistem persamaan berikut menggunakan Eliminasi Gauss dengan Partial Pivoting:

$$
\begin{aligned}
2x_2 + 3x_3 &= 8 \\
4x_1 + 6x_2 + 7x_3 &= -3 \\
2x_1 - 3x_2 + 6x_3 &= 5
\end{aligned}
$$

Representasi matriks augmented awal:

$$
[A | b] = \left[ \begin{array}{ccc|c}
0 & 2 & 3 & 8 \\
4 & 6 & 7 & -3 \\
2 & -3 & 6 & 5
\end{array} \right]
$$

### Langkah 1: Kolom 1 ($k=1$)
* Elemen pivot potensial pada kolom 1 adalah: baris 1 ($|0|$), baris 2 ($|4|$), baris 3 ($|2|$).
* Nilai mutlak terbesar berada pada baris 2 ($4$). Maka, tukar baris 1 dan baris 2:
  $$
  \left[ \begin{array}{ccc|c}
  4 & 6 & 7 & -3 \\
  0 & 2 & 3 & 8 \\
  2 & -3 & 6 & 5
  \end{array} \right]
  $$
* Eliminasi baris di bawah pivot (baris 2 sudah nol di kolom 1):
  * Untuk baris 3: faktor pengali $m_{31} = 2/4 = 0.5$.
  * Baris 3 baru: $\text{Baris 3} - 0.5 \times \text{Baris 1}$
    $$R_3 \leftarrow [2, -3, 6 | 5] - 0.5 \times [4, 6, 7 | -3] = [0, -6, 2.5 | 6.5]$$
  * Matriks terupdate:
    $$
    \left[ \begin{array}{ccc|c}
    4 & 6 & 7 & -3 \\
    0 & 2 & 3 & 8 \\
    0 & -6 & 2.5 & 6.5
    \end{array} \right]
    $$

### Langkah 2: Kolom 2 ($k=2$)
* Elemen pivot potensial pada kolom 2 (baris 2 ke bawah) adalah: baris 2 ($|2|$), baris 3 ($|-6|$).
* Nilai mutlak terbesar berada pada baris 3 ($6$). Tukar baris 2 dan baris 3:
  $$
  \left[ \begin{array}{ccc|c}
  4 & 6 & 7 & -3 \\
  0 & -6 & 2.5 & 6.5 \\
  0 & 2 & 3 & 8
  \end{array} \right]
  $$
* Eliminasi baris di bawah pivot (baris 3):
  * Faktor pengali $m_{32} = 2 / (-6) = -1/3 \approx -0.3333$.
  * Baris 3 baru: $\text{Baris 3} - (-1/3) \times \text{Baris 2}$
    $$R_3 \leftarrow [0, 2, 3 | 8] + \frac{1}{3} \times [0, -6, 2.5 | 6.5] = [0, 0, 3.8333 | 10.1667]$$
  * Matriks segitiga atas akhir:
    $$
    \left[ \begin{array}{ccc|c}
    4 & 6 & 7 & -3 \\
    0 & -6 & 2.5 & 6.5 \\
    0 & 0 & 3.8333 & 10.1667
    \end{array} \right]
    $$

### Langkah 3: Substitusi Mundur
* Cari $x_3$:
  $$x_3 = \frac{10.1667}{3.8333} = 2.65217$$
* Cari $x_2$:
  $$-6x_2 + 2.5(2.65217) = 6.5 \implies -6x_2 = 6.5 - 6.6304 \implies x_2 = 0.02174$$
* Cari $x_1$:
  $$4x_1 + 6(0.02174) + 7(2.65217) = -3 \implies 4x_1 = -3 - 0.1304 - 18.5652 \implies x_1 = -5.4239$$

---

## 4. Panduan Penggunaan Skrip Python

Modul Python [01_eliminasi_gauss.py](file:///d:/My%20Project/physics/Physics_Dev/01_Metode_Numerik/01_Sistem_Persamaan_Linier/Python/01_eliminasi_gauss.py) menyediakan fungsi `eliminasi_gauss(A, b)` yang diimplementasikan dari dasar menggunakan *numpy*.

### Cara Import dan Eksekusi:

```python
import numpy as np
from Python.01_eliminasi_gauss import eliminasi_gauss

# Definisikan matriks A dan vektor b
A = np.array([
    [0.0, 2.0, 3.0],
    [4.0, 6.0, 7.0],
    [2.0, -3.0, 6.0]
], dtype=float)

b = np.array([8.0, -3.0, 5.0], dtype=float)

# Selesaikan SPL
try:
    x = eliminasi_gauss(A, b)
    print("Solusi x:", x)
except ValueError as e:
    print("Kesalahan:", e)
```
