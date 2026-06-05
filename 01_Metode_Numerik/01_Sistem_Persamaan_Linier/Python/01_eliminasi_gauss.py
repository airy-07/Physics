"""
Modul Penyelesaian Sistem Persamaan Linier (SPL) dengan Eliminasi Gauss.
Diimplementasikan secara mandiri menggunakan NumPy untuk tujuan pembelajaran.
"""
import numpy as np

def eliminasi_gauss(A, b, verbose=False):
    """
    Menyelesaikan SPL Ax = b menggunakan metode Eliminasi Gauss dengan Partial Pivoting.
    
    Parameter:
    -----------
    A : numpy.ndarray (2D)
        Matriks koefisien berukuran N x N.
    b : numpy.ndarray (1D)
        Vektor konstanta berukuran N.
    verbose : bool, opsional
        Jika True, menampilkan langkah-langkah perhitungan secara detail (default: False).
        
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
        
    # Fungsi pembantu untuk mencetak matriks augmented
    def cetak_augmented(mat_A, vec_b):
        for idx in range(n):
            row_str = "  [" + " ".join(f"{val:8.4f}" for val in mat_A[idx]) + " | " + f"{vec_b[idx]:8.4f}" + "]"
            print(row_str)

    if verbose:
        print("\nMatriks Augmented Awal [A | b]:")
        cetak_augmented(A_mod, b_mod)
        print("-" * 60)

    # --- Tahap 1: Eliminasi Maju dengan Partial Pivoting ---
    for k in range(n):
        if verbose:
            print(f"\n--- LANGKAH ELEMINASI KOLOM {k+1} ---")
            
        # 1. Pencarian Pivot Sebagian (Partial Pivoting)
        pivot_row = k + np.argmax(np.abs(A_mod[k:, k]))
        
        # Cek jika nilai pivot sangat dekat dengan nol (singular)
        if np.abs(A_mod[pivot_row, k]) < 1e-12:
            raise ValueError("Matriks singular atau tidak memiliki solusi unik (pembagian dengan nol terdeteksi).")
            
        # Tukar baris k dengan pivot_row jika berbeda
        if pivot_row != k:
            if verbose:
                print(f"  * Nilai pivot terbesar pada kolom {k+1} berada di Baris {pivot_row+1} ({A_mod[pivot_row, k]:.4f}).")
                print(f"  * Menukar Baris {k+1} dengan Baris {pivot_row+1}...")
            A_mod[[k, pivot_row]] = A_mod[[pivot_row, k]]
            b_mod[[k, pivot_row]] = b_mod[[pivot_row, k]]
            if verbose:
                cetak_augmented(A_mod, b_mod)
        else:
            if verbose:
                print(f"  * Baris {k+1} sudah memuat nilai pivot terbesar ({A_mod[k, k]:.4f}). Tidak ada baris yang ditukar.")
            
        # 2. Eliminasi elemen di bawah diagonal
        eliminated_any = False
        for i in range(k + 1, n):
            factor = A_mod[i, k] / A_mod[k, k]
            if np.abs(factor) > 1e-15:
                eliminated_any = True
                if verbose:
                    print(f"  * Operasi Baris: Baris {i+1} <- Baris {i+1} - ({factor:.4f}) * Baris {k+1}")
                A_mod[i, k:] -= factor * A_mod[k, k:]
                b_mod[i] -= factor * b_mod[k]
                A_mod[i, k] = 0.0 # Bersihkan nilai di bawah diagonal agar presisi 0

        if verbose:
            if eliminated_any:
                print("  * Hasil Matriks Augmented setelah eliminasi:")
                cetak_augmented(A_mod, b_mod)
            else:
                print("  * Seluruh elemen di bawah diagonal sudah nol. Langkah eliminasi dilewati.")
            
    # --- Tahap 2: Substitusi Mundur ---
    if verbose:
        print("\n" + "=" * 60)
        print("TAHAP SUBSTITUSI MUNDUR")
        print("=" * 60)
        
    x = np.zeros(n)
    
    # Hitung variabel terakhir
    x[n - 1] = b_mod[n - 1] / A_mod[n - 1, n - 1]
    if verbose:
        print(f"  * x[{n}] = {b_mod[n-1]:.4f} / {A_mod[n-1, n-1]:.4f} = {x[n-1]:.6f}")
    
    # Hitung variabel lainnya dari bawah ke atas
    for i in range(n - 2, -1, -1):
        sum_terms = np.dot(A_mod[i, (i + 1):], x[(i + 1):])
        x[i] = (b_mod[i] - sum_terms) / A_mod[i, i]
        if verbose:
            # Format rumus detail untuk log verbose
            terms_str = " + ".join(f"({A_mod[i, j]:.4f} * {x[j]:.4f})" for j in range(i+1, n))
            print(f"  * x[{i+1}] = ({b_mod[i]:.4f} - [{terms_str}]) / {A_mod[i, i]:.4f} = {x[i]:.6f}")
        
    return x

if __name__ == '__main__':
    print("=" * 60)
    print("SOLVER SPL - METODE ELIMINASI GAUSS")
    print("=" * 60)
    
    try:
        # Masukan ukuran matriks
        n = int(input("Masukkan jumlah baris/kolom matriks (N): "))
        
        # Masukan elemen matriks A
        print("\nMasukkan matriks koefisien A baris demi baris (pisahkan angka dengan spasi):")
        A_rows = []
        for i in range(n):
            row = list(map(float, input(f"Baris {i+1}: ").split()))
            if len(row) != n:
                raise ValueError(f"Baris harus memiliki tepat {n} elemen.")
            A_rows.append(row)
        A = np.array(A_rows)
        
        # Masukan elemen vektor b
        print(f"\nMasukkan vektor konstanta b ({n} angka dipisahkan dengan spasi):")
        b = np.array(list(map(float, input("b: ").split())))
        if len(b) != n:
            raise ValueError(f"Vektor b harus memiliki tepat {n} elemen.")
            
        print("\nMatriks A:")
        print(A)
        print("Vektor b:")
        print(b)
        
        # Selesaikan SPL
        x = eliminasi_gauss(A, b, verbose=True)
        
        print("\n" + "-" * 40)
        print("SOLUSI (x):")
        print("-" * 40)
        for i in range(n):
            print(f"x[{i+1}] = {x[i]:.6f}")
            
        # Verifikasi dengan np.linalg.solve
        x_np = np.linalg.solve(A, b)
        selisih = np.linalg.norm(x - x_np)
        print(f"\nVerifikasi (Selisih Norm dengan NumPy solver): {selisih:.2e}")
        print("=" * 60)
        
    except ValueError as e:
        print(f"\nKesalahan input: {e}")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {e}")
