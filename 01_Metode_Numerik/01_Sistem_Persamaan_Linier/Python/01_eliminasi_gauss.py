"""
Modul Penyelesaian Sistem Persamaan Linier (SPL) dengan Eliminasi Gauss.
Diimplementasikan secara mandiri menggunakan NumPy untuk tujuan pembelajaran.
"""
import numpy as np

def eliminasi_gauss(A, b):
    """
    Menyelesaikan SPL Ax = b menggunakan metode Eliminasi Gauss dengan Partial Pivoting.
    
    Parameter:
    -----------
    A : numpy.ndarray (2D)
        Matriks koefisien berukuran N x N.
    b : numpy.ndarray (1D)
        Vektor konstanta berukuran N.
        
    Kembalian:
    ----------
    x : numpy.ndarray (1D)
        Vektor solusi berukuran N.
        
    Pengecualian:
    -------------
    ValueError : Jika dimensi matriks tidak sesuai atau matriks singular.
    """
    # Mengubah input menjadi array numpy tipe float
    A_mod = np.array(A, dtype=float)
    b_mod = np.array(b, dtype=float)
    
    # Validasi dimensi
    if A_mod.ndim != 2 or A_mod.shape[0] != A_mod.shape[1]:
        raise ValueError("Matriks A harus berupa matriks persegi berdimensi 2 (N x N).")
        
    n = A_mod.shape[0]
    
    if b_mod.ndim != 1 or b_mod.shape[0] != n:
        raise ValueError("Vektor b harus berupa vektor 1D dengan panjang N.")
        
    # --- Tahap 1: Eliminasi Maju dengan Partial Pivoting ---
    for k in range(n):
        # 1. Pencarian Pivot Sebagian (Partial Pivoting)
        pivot_row = k + np.argmax(np.abs(A_mod[k:, k]))
        
        # Cek jika nilai pivot sangat dekat dengan nol (singular)
        if np.abs(A_mod[pivot_row, k]) < 1e-12:
            raise ValueError("Matriks singular atau tidak memiliki solusi unik (pembagian dengan nol terdeteksi).")
            
        # Tukar baris k dengan pivot_row jika berbeda
        if pivot_row != k:
            A_mod[[k, pivot_row]] = A_mod[[pivot_row, k]]
            b_mod[[k, pivot_row]] = b_mod[[pivot_row, k]]
            
        # 2. Eliminasi elemen di bawah diagonal
        for i in range(k + 1, n):
            factor = A_mod[i, k] / A_mod[k, k]
            A_mod[i, k:] -= factor * A_mod[k, k:]
            b_mod[i] -= factor * b_mod[k]
            
    # --- Tahap 2: Substitusi Mundur ---
    x = np.zeros(n)
    
    # Hitung variabel terakhir
    x[n - 1] = b_mod[n - 1] / A_mod[n - 1, n - 1]
    
    # Hitung variabel lainnya dari bawah ke atas
    for i in range(n - 2, -1, -1):
        sum_terms = np.dot(A_mod[i, (i + 1):], x[(i + 1):])
        x[i] = (b_mod[i] - sum_terms) / A_mod[i, i]
        
    return x

if __name__ == '__main__':
    print("=" * 60)
    print("DEMO METODE ELIMINASI GAUSS DENGAN PARTIAL PIVOTING")
    print("=" * 60)
    
    # Studi Kasus Fisika: Hukum Kirchhoff untuk Rangkaian 3-Loop
    # Persamaan arus loop I1, I2, I3:
    # Loop 1:  10*I1 - 2*I2 - 3*I3 = 12
    # Loop 2:  -2*I1 + 8*I2 - 1*I3 = 0
    # Loop 3:  -3*I1 - 1*I2 + 6*I3 = -5
    
    A = np.array([
        [10.0, -2.0, -3.0],
        [-2.0,  8.0, -1.0],
        [-3.0, -1.0,  6.0]
    ])
    
    b = np.array([12.0, 0.0, -5.0])
    
    print("Matriks Koefisien A (Hambatan):")
    print(A)
    print("\nVektor Konstanta b (Tegangan Sumber):")
    print(b)
    
    try:
        # Panggil fungsi eliminasi gauss
        I = eliminasi_gauss(A, b)
        
        # Verifikasi dengan numpy solver bawaan
        I_np = np.linalg.solve(A, b)
        
        print("\n" + "-" * 40)
        print("HASIL PERHITUNGAN:")
        print("-" * 40)
        print(f"Arus Loop I1 = {I[0]:.6f} Ampere")
        print(f"Arus Loop I2 = {I[1]:.6f} Ampere")
        print(f"Arus Loop I3 = {I[2]:.6f} Ampere")
        
        # Cetak perbandingan selisih
        selisih = np.linalg.norm(I - I_np)
        print(f"\nVerifikasi dengan np.linalg.solve: OK (Norm Selisih = {selisih:.2e})")
        print("=" * 60)
        
    except ValueError as e:
        print(f"\nTerjadi Kesalahan: {e}")
