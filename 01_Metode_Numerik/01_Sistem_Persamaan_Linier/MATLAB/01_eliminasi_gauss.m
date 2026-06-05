function x = eliminasi_gauss(A, b, verbose)
    % ELIMINASI_GAUSS Menyelesaikan SPL Ax = b menggunakan metode Eliminasi Gauss.
    %
    % Sintaks:
    %   x = 01_eliminasi_gauss()             -> Menjalankan demo interaktif
    %   x = 01_eliminasi_gauss(A, b)         -> Menyelesaikan SPL tanpa verbose
    %   x = 01_eliminasi_gauss(A, b, true)   -> Menyelesaikan SPL dengan verbose
    
    if nargin == 0
        % --- DEMO INTERAKTIF ---
        fprintf('=======================================================\n');
        fprintf(' SOLVER SPL - METODE ELIMINASI GAUSS (MATLAB/OCTAVE)\n');
        fprintf('=======================================================\n');
        
        try
            n = input('Masukkan jumlah baris/kolom matriks (N): ');
            if isempty(n) || n <= 0
                error('N harus berupa bilangan bulat positif.');
            end
            
            fprintf('\nMasukkan matriks koefisien A baris demi baris:\n');
            A_demo = zeros(n, n);
            for i = 1:n
                row = input(sprintf('  Baris %d (pisahkan angka dengan spasi): ', i));
                if length(row) ~= n
                    error('Jumlah elemen baris harus sama dengan %d.', n);
                end
                A_demo(i, :) = row;
            end
            
            fprintf('\nMasukkan vektor konstanta b (%d angka dipisahkan dengan spasi):\n', n);
            b_demo = input('  b: ');
            if length(b_demo) ~= n
                error('Vektor b harus memiliki tepat %d elemen.', n);
            end
            b_demo = b_demo(:); % Paksa menjadi vektor kolom
            
            fprintf('\nTampilkan langkah-langkah perhitungan? (y/n): ');
            show_steps_str = input('', 's');
            show_steps = strcmpi(strtrim(show_steps_str), 'y');
            
            fprintf('\nMatriks A:\n');
            disp(A_demo);
            fprintf('Vektor b:\n');
            disp(b_demo);
            
            % Selesaikan SPL
            x_sol = run_solver(A_demo, b_demo, show_steps);
            
            fprintf('\n----------------------------------------\n');
            fprintf(' SOLUSI (x):\n');
            fprintf('----------------------------------------\n');
            for i = 1:n
                fprintf('  x(%d) = %6.6f\n', i, x_sol(i));
            end
            
            % Verifikasi dengan solver bawaan MATLAB/Octave (\)
            x_ref = A_demo \ b_demo;
            selisih = norm(x_sol - x_ref);
            fprintf('\nVerifikasi (Selisih Norm dengan MATLAB solver): %2.2e\n', selisih);
            fprintf('=======================================================\n');
            
            if nargout > 0
                x = x_sol;
            end
        catch ME
            fprintf('\nTerjadi kesalahan: %s\n', ME.message);
        end
        return;
    end
    
    % --- EKSEKUSI FUNGSIONAL ---
    if nargin < 3
        verbose = false;
    end
    
    b = b(:); % Paksa b menjadi vektor kolom
    x = run_solver(A, b, verbose);
end

function x = run_solver(A, b, verbose)
    % Fungsi utama penyelesaian SPL
    A_mod = double(A);
    b_mod = double(b);
    
    [rows, cols] = size(A_mod);
    if rows ~= cols
        error('Matriks A harus berupa matriks persegi (N x N).');
    end
    
    n = rows;
    if length(b_mod) ~= n
        error('Vektor b harus memiliki panjang N.');
    end
    
    if verbose
        fprintf('\n=======================================================\n');
        fprintf(' LANGKAH-LANGKAH NUMERIK: ELIMINASI MAJU\n');
        fprintf('=======================================================\n');
        fprintf('\nMatriks Augmented Awal [A │ b]:\n');
        cetak_augmented(A_mod, b_mod);
        fprintf('-------------------------------------------------------\n');
    end
    
    % --- Tahap 1: Eliminasi Maju dengan Partial Pivoting ---
    for k = 1:n
        if verbose
            fprintf('\n👉 [Langkah %d] Kolom %d:\n', k, k);
        end
        
        % 1. Pencarian Pivot Sebagian (Partial Pivoting)
        [max_val, pivot_row_idx] = max(abs(A_mod(k:n, k)));
        pivot_row = pivot_row_idx + k - 1;
        
        if max_val < 1e-12
            error('Matriks singular atau tidak memiliki solusi unik (pembagian dengan nol terdeteksi).');
        end
        
        % Tukar baris k dengan pivot_row jika berbeda
        if pivot_row ~= k
            if verbose
                fprintf('  * 🔄 Tukar Baris %d <-> Baris %d (karena |%6.4f| terbesar pada kolom %d)\n', k, pivot_row, A_mod(pivot_row, k), k);
            end
            temp_A = A_mod(k, :);
            A_mod(k, :) = A_mod(pivot_row, :);
            A_mod(pivot_row, :) = temp_A;
            
            temp_b = b_mod(k);
            b_mod(k) = b_mod(pivot_row);
            b_mod(pivot_row) = temp_b;
            
            if verbose
                cetak_augmented(A_mod, b_mod);
            end
        else
            if verbose
                fprintf('  * ✔️ Baris %d sudah memuat pivot terbesar (%6.4f). Tidak ada baris ditukar.\n', k, A_mod(k, k));
            end
        end
        
        % 2. Eliminasi elemen di bawah diagonal
        eliminated_any = false;
        for i = k+1:n
            factor = A_mod(i, k) / A_mod(k, k);
            if abs(factor) > 1e-15
                eliminated_any = true;
                if verbose
                    fprintf('  * ⚙️ OBE: Baris %d <- Baris %d - (%6.4f) * Baris %d\n', i, i, factor, k);
                end
                A_mod(i, k:n) = A_mod(i, k:n) - factor * A_mod(k, k:n);
                b_mod(i) = b_mod(i) - factor * b_mod(k);
                A_mod(i, k) = 0.0; % Pastikan tepat nol secara numerik
            end
        end
        
        if verbose
            if eliminated_any
                fprintf('  * Hasil matriks setelah eliminasi kolom:\n');
                cetak_augmented(A_mod, b_mod);
            else
                fprintf('  * Elemen di bawah diagonal kolom ini sudah nol.\n');
            end
        end
    end
    
    % --- Tahap 2: Substitusi Mundur ---
    if verbose
        fprintf('\n=======================================================\n');
        fprintf(' LANGKAH-LANGKAH NUMERIK: SUBSTITUSI MUNDUR\n');
        fprintf('=======================================================\n');
    end
    
    x = zeros(n, 1);
    
    % Hitung variabel terakhir
    x(n) = b_mod(n) / A_mod(n, n);
    if verbose
        fprintf('  * x(%d) = %6.4f / %6.4f = %6.6f\n', n, b_mod(n), A_mod(n, n), x(n));
    end
    
    % Hitung variabel lainnya dari bawah ke atas
    for i = n-1:-1:1
        sum_terms = A_mod(i, i+1:n) * x(i+1:n);
        x(i) = (b_mod(i) - sum_terms) / A_mod(i, i);
        if verbose
            fprintf('  * x(%d) = (%6.4f - (%6.4f)) / %6.4f = %6.6f\n', i, b_mod(i), sum_terms, A_mod(i, i), x(i));
        end
    end
end

function cetak_augmented(mat_A, vec_b)
    n = size(mat_A, 1);
    for idx = 1:n
        A_row = mat_A(idx, :);
        A_row(abs(A_row) < 1e-12) = 0; % Bersihkan -0.0
        b_val = vec_b(idx);
        if abs(b_val) < 1e-12
            b_val = 0;
        end
        
        % Buat format string untuk seluruh kolom A_row
        coef_str = '';
        for col = 1:length(A_row)
            coef_str = [coef_str, sprintf('%9.4f ', A_row(col))];
        end
        fprintf('    [ %s │  %9.4f ]\n', coef_str, b_val);
    end
end
