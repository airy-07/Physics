# Progres Pengerjaan & Migrasi (Physics_Dev -> Physics)

Dokumen ini digunakan untuk memantau progres pengerjaan berkas dan migrasi dari repositori privat (`Physics_Dev`) ke repositori publik (`Physics`).

### Petunjuk Penggunaan:
- `[ ]` : **Belum Dikerjakan** (Belum ada di privat maupun publik).
- `[x]` : **Selesai & Sinkron** (Sudah selesai di `Physics_Dev` dan isinya sama persis dengan `Physics` publik).
- `[~]` : **Sedang Direvisi / Belum Sinkron** (Sudah ada di repo publik, tetapi versi privat memiliki perubahan baru yang belum di-upload).

### Panduan Alur Kerja Sehari-hari (Git & Progress Cheat Sheet)

#### A. Saat Sedang Mengerjakan/Merevisi Kode (Repo Privat)
1. Anda bebas mengedit berkas di dalam `Physics_Dev`.
2. Jika ada berkas yang Anda ubah dan belum sempat di-upload ke publik, ubah statusnya di `PROGRES.md` menjadi `[~]` (Sedang Direvisi).
3. Simpan revisi Anda ke repo privat (GitHub `Physics_Dev`):
   ```bash
   git add .
   git commit -m "merevisi metode [nama_berkas]"
   git push origin main
   ```

#### B. Mengetahui Perbedaan Antara Privat dan Publik (Pelacakan Otomatis)
Jika Anda lupa berkas mana saja yang isinya berbeda antara repo privat (`Physics_Dev`) dan publik (`Physics`), Anda bisa mengetik perintah ini di terminal:
```bash
git fetch public
git diff public/main --name-only
```
*Perintah ini akan langsung memunculkan daftar nama berkas yang telah Anda revisi di privat namun belum ada di publik!*

#### C. Saat Hasil Revisi Sudah Sesuai Keinginan (Upload ke Publik)
Setelah hasil revisi stabil dan Anda ingin mempublikasikannya ke repo publik:
1. Tandai kembali berkas tersebut menjadi `[x]` di `PROGRES.md`.
2. Jalankan perintah push ke remote publik:
   ```bash
   git add PROGRES.md
   git commit -m "sinkronisasi progres ke publik"
   git push public main
   ```
   *(Atau Anda cukup memberi tahu AI: **"Tolong sinkronkan revisi terbaru ke repo publik"**, dan AI akan melakukannya untuk Anda.)*

---

## Daftar Checklist Progres

- [x] **📁 00_Pendahuluan/**
  - [x] 01_instalasi_python.md
  - [x] 02_instalasi_matlab_octave.md
  - [x] 03_penggunaan_jupyter.md
  - [x] 04_struktur_repo.md
  - [x] 05_panduan_kontribusi.md
- [ ] **📁 01_Metode_Numerik/**
  - [ ] **📁 01_Sistem_Persamaan_Linier/**
    - [ ] **📁 Excel/**
      - [ ] 05_iterasi_jacobi.xlsx
      - [ ] 06_iterasi_gauss_seidel.xlsx
    - [ ] **📁 MATLAB/**
      - [ ] 01_eliminasi_gauss.m
      - [ ] 02_eliminasi_gauss_jordan.m
      - [ ] 03_dekomposisi_lu.m
      - [ ] 05_iterasi_jacobi.m
      - [ ] 06_iterasi_gauss_seidel.m
    - [ ] **📁 Python/**
      - [x] 01_eliminasi_gauss.py
      - [ ] 02_eliminasi_gauss_jordan.py
      - [ ] 03_dekomposisi_lu.py
      - [ ] 04_dekomposisi_cholesky.py
      - [ ] 05_iterasi_jacobi.py
      - [ ] 06_iterasi_gauss_seidel.py
      - [ ] 07_sor.py
      - [ ] 08_conjugate_gradient.py
      - [ ] 09_gmres.py
      - [ ] 10_biconjugate_gradient.py
      - [ ] 11_dekomposisi_qr.py
      - [ ] 12_pseudoinverse_svd.py
  - [ ] **📁 02_Pencarian_Akar/**
    - [ ] **📁 Excel/**
      - [ ] 01_metode_bisection.xlsx
      - [ ] 03_metode_newton_raphson.xlsx
    - [ ] **📁 MATLAB/**
      - [ ] 01_metode_bisection.m
      - [ ] 03_metode_newton_raphson.m
    - [ ] **📁 Python/**
      - [ ] 01_metode_bisection.py
      - [ ] 02_metode_regula_falsi.py
      - [ ] 03_metode_newton_raphson.py
      - [ ] 04_metode_secant.py
      - [ ] 05_iterasi_titik_tetap.py
      - [ ] 06_akar_polinomial.py
  - [ ] **📁 03_Interpolasi_dan_Aproksimasi/**
    - [ ] **📁 Excel/**
      - [ ] 06_least_square.xlsx
    - [ ] **📁 MATLAB/**
      - [ ] 03_interpolasi_lagrange.m
      - [ ] 06_least_square.m
    - [ ] **📁 Python/**
      - [ ] 01_interpolasi_linier.py
      - [ ] 02_interpolasi_polinomial.py
      - [ ] 03_interpolasi_lagrange.py
      - [ ] 04_newton_divided_difference.py
      - [ ] 05_spline_kubik.py
      - [ ] 06_least_square.py
      - [ ] 07_curve_fitting.py
  - [ ] **📁 04_Diferensiasi_Numerik/**
    - [ ] **📁 MATLAB/**
      - [ ] 03_central_difference.m
    - [ ] **📁 Python/**
      - [ ] 01_forward_difference.py
      - [ ] 02_backward_difference.py
      - [ ] 03_central_difference.py
      - [ ] 04_second_derivative.py
      - [ ] 05_richardson_extrapolation.py
  - [ ] **📁 05_Integrasi_Numerik/**
    - [ ] **📁 Excel/**
      - [ ] 01_aturan_trapesium.xlsx
      - [ ] 02_aturan_simpson_1_3.xlsx
    - [ ] **📁 MATLAB/**
      - [ ] 01_aturan_trapesium.m
      - [ ] 02_aturan_simpson_1_3.m
    - [ ] **📁 Python/**
      - [ ] 01_aturan_trapesium.py
      - [ ] 02_aturan_simpson_1_3.py
      - [ ] 03_aturan_simpson_3_8.py
      - [ ] 04_aturan_boole.py
      - [ ] 05_integrasi_romberg.py
      - [ ] 06_kuadratur_gauss_legendre.py
      - [ ] 07_integrasi_monte_carlo.py
      - [ ] 08_adaptive_simpson.py
      - [ ] 09_gauss_laguerre.py
      - [ ] 10_gauss_hermite.py
  - [ ] **📁 06_Persamaan_Diferensial_Biasa_ODE/**
    - [ ] **📁 Excel/**
      - [ ] 01_metode_euler.xlsx
    - [ ] **📁 MATLAB/**
      - [ ] 01_metode_euler.m
      - [ ] 05_runge_kutta_4.m
    - [ ] **📁 Python/**
      - [ ] 01_metode_euler.py
      - [ ] 02_metode_heun.py
      - [ ] 03_metode_midpoint.py
      - [ ] 04_runge_kutta_2.py
      - [ ] 05_runge_kutta_4.py
      - [ ] 06_adaptive_rk45.py
      - [ ] 07_predictor_corrector.py
      - [ ] 08_sistem_ode.py
  - [ ] **📁 07_Persamaan_Diferensial_Parsial_PDE/**
    - [ ] **📁 MATLAB/**
      - [ ] 01_persamaan_panas_1d.m
      - [ ] 05_persamaan_laplace.m
    - [ ] **📁 Python/**
      - [ ] 01_persamaan_panas_1d.py
      - [ ] 02_persamaan_panas_2d.py
      - [ ] 03_persamaan_gelombang_1d.py
      - [ ] 04_persamaan_gelombang_2d.py
      - [ ] 05_persamaan_laplace.py
      - [ ] 06_persamaan_poisson.py
      - [ ] 07_diffusion_equation.py
      - [ ] 08_advection_diffusion.py
  - [ ] **📁 08_Optimisasi_Numerik/**
    - [ ] **📁 MATLAB/**
      - [ ] 01_gradient_descent.m
    - [ ] **📁 Python/**
      - [ ] 01_gradient_descent.py
      - [ ] 02_newton_optimization.py
      - [ ] 03_conjugate_gradient_optimization.py
      - [ ] 04_golden_section_search.py
      - [ ] 05_simulated_annealing.py
      - [ ] 06_genetic_algorithm.py
- [ ] **📁 02_Fisika_Komputasi/**
  - [ ] **📁 01_Mekanika_Klasik/**
    - [ ] **📁 MATLAB/**
      - [ ] 04_osilator_harmonik.m
      - [ ] 06_pendulum_sederhana.m
    - [ ] **📁 Python/**
      - [ ] 01_gerak_lurus.py
      - [ ] 02_gerak_jatuh_bebas.py
      - [ ] 03_gerak_parabola.py
      - [ ] 04_osilator_harmonik.py
      - [ ] 05_osilator_teredam.py
      - [ ] 06_pendulum_sederhana.py
      - [ ] 07_pendulum_ganda.py
      - [ ] 08_gerak_planet.py
      - [ ] 09_three_body_problem.py
      - [ ] 10_energi_potensial.py
      - [ ] 11_analisis_gaya_mekanik.py
      - [ ] 12_perhitungan_torsi_motor.py
  - [ ] **📁 02_Elektromagnetisme/**
    - [ ] **📁 MATLAB/**
      - [ ] 01_medan_listrik_muatan_titik.m
      - [ ] 08_persamaan_poisson_listrik.m
    - [ ] **📁 Python/**
      - [ ] 01_medan_listrik_muatan_titik.py
      - [ ] 02_potensial_listrik.py
      - [ ] 03_medan_dipol_listrik.py
      - [ ] 04_hukum_gauss.py
      - [ ] 05_kapasitor_pelat_sejajar.py
      - [ ] 06_medan_magnet_kawat_lurus.py
      - [ ] 07_hukum_biot_savart.py
      - [ ] 08_persamaan_poisson_listrik.py
      - [ ] 09_gelombang_elektromagnetik.py
  - [ ] **📁 03_Fisika_Fluida/**
    - [ ] **📁 MATLAB/**
      - [ ] profil_kecepatan_aliran.m
    - [ ] **📁 Python/**
      - [ ] 01_hukum_bernoulli.py
      - [ ] 02_aliran_pipa.py
      - [ ] 03_profil_poiseuille.py
      - [ ] 04_persamaan_kontinuitas.py
      - [ ] 05_difusi_zat_cair.py
      - [ ] 06_advection_diffusion_fluid.py
      - [ ] 07_lattice_boltzmann_2d.py
  - [ ] **📁 04_Termodinamika_dan_Fisika_Statistik/**
    - [ ] **📁 MATLAB/**
      - [ ] 05_monte_carlo_pi.m
    - [ ] **📁 Python/**
      - [ ] 01_hukum_gas_ideal.py
      - [ ] 02_distribusi_maxwell_boltzmann.py
      - [ ] 03_random_walk_1d.py
      - [ ] 04_random_walk_2d.py
      - [ ] 05_monte_carlo_pi.py
      - [ ] 06_model_ising_1d.py
      - [ ] 07_model_ising_2d.py
      - [ ] 08_simulated_annealing_fisika.py
  - [ ] **📁 05_Mekanika_Kuantum/**
    - [ ] **📁 MATLAB/**
      - [ ] 04_schrodinger_finite_difference.m
    - [ ] **📁 Python/**
      - [ ] 01_partikel_dalam_kotak_1d.py
      - [ ] 02_osilator_harmonik_kuantum.py
      - [ ] 03_tunneling_effect.py
      - [ ] 04_schrodinger_finite_difference.py
      - [ ] 05_potensial_sumur_hingga.py
      - [ ] 06_metode_variational.py
      - [ ] 07_wave_packet_evolution.py
  - [ ] **📁 06_Astrofisika_dan_Gravitasi/**
    - [ ] **📁 MATLAB/**
      - [ ] 02_orbit_planet.m
    - [ ] **📁 Python/**
      - [ ] 01_hukum_kepler.py
      - [ ] 02_orbit_planet.py
      - [ ] 03_orbit_biner.py
      - [ ] 04_n_body_simulation.py
      - [ ] 05_kecepatan_lepas.py
      - [ ] 06_kurva_rotasi_galaksi.py
  - [ ] **📁 07_Fisika_Lingkungan/**
    - [ ] **📁 MATLAB/**
      - [ ] 04_model_energi_surya.m
    - [ ] **📁 Python/**
      - [ ] 01_model_distribusi_cahaya_lux_par.py
      - [ ] 02_model_penyebaran_polutan.py
      - [ ] 03_model_suhu_harian.py
      - [ ] 04_model_energi_surya.py
      - [ ] 05_model_kualitas_udara.py
      - [ ] 06_model_difusi_panas_lingkungan.py
      - [ ] 07_model_radiasi_matahari.py
  - [ ] **📁 08_Fisika_Modern_dan_Relativitas/**
    - [ ] **📁 MATLAB/**
      - [ ] 05_radiasi_benda_hitam.m
    - [ ] **📁 Python/**
      - [ ] 01_dilatasi_waktu.py
      - [ ] 02_kontraksi_panjang.py
      - [ ] 03_energi_relativistik.py
      - [ ] 04_efek_fotolistrik.py
      - [ ] 05_radiasi_benda_hitam.py
      - [ ] 06_distribusi_planck.py
- [ ] **📁 03_Scientific_Computing/**
  - [ ] **📁 01_Visualisasi_Data/**
    - [ ] **📁 MATLAB/**
      - [ ] 01_plot_dasar.m
      - [ ] 03_plot_3d.m
    - [ ] **📁 Python/**
      - [ ] 01_plot_dasar.py
      - [ ] 02_subplot.py
      - [ ] 03_plot_3d.py
      - [ ] 04_heatmap_2d.py
      - [ ] 05_contour_plot.py
      - [ ] 06_animasi_pendulum.py
      - [ ] 07_animasi_orbit.py
      - [ ] 08_animasi_gelombang.py
  - [ ] **📁 02_Data_Fitting_dan_Regresi/**
    - [ ] **📁 Excel/**
      - [ ] 01_regresi_linier.xlsx
      - [ ] 06_chi_square_fit.xlsx
    - [ ] **📁 Python/**
      - [ ] 01_regresi_linier.py
      - [ ] 02_regresi_polinomial.py
      - [ ] 03_exponential_fit.py
      - [ ] 04_gaussian_fit.py
      - [ ] 05_curve_fit_scipy.py
      - [ ] 06_chi_square_fit.py
      - [ ] 07_fitting_data_eksperimen.py
  - [ ] **📁 03_Analisis_Error/**
    - [ ] **📁 Excel/**
      - [ ] 02_propagasi_error.xlsx
    - [ ] **📁 Python/**
      - [ ] 01_error_absolut_relatif.py
      - [ ] 02_propagasi_error.py
      - [ ] 03_standard_deviation.py
      - [ ] 04_standard_error.py
      - [ ] 05_chi_square.py
      - [ ] 06_uncertainty_plot.py
  - [ ] **📁 04_Komputasi_Paralel/**
    - [ ] **📁 MATLAB/**
      - [ ] 01_parallel_loop.m
    - [ ] **📁 Python/**
      - [ ] 01_multiprocessing_dasar.py
      - [ ] 02_parallel_monte_carlo.py
      - [ ] 03_numba_acceleration.py
      - [ ] 04_vectorization_numpy.py
      - [ ] 05_gpu_cupy.py
      - [ ] 06_benchmark_runtime.py
  - [ ] **📁 05_Manajemen_Data_Ilmiah/**
    - [ ] **📁 Dataset_Contoh/**
      - [ ] data_intensitas_cahaya.csv
      - [ ] data_osilator.csv
      - [ ] data_suhu_harian.csv
    - [ ] **📁 Python/**
      - [ ] 01_baca_csv.py
      - [ ] 02_baca_excel.py
      - [ ] 03_baca_json.py
      - [ ] 04_simpan_hasil_simulasi.py
      - [ ] 05_logging_eksperimen.py
- [ ] **📁 04_Proyek_Aplikasi/**
  - [ ] **📁 01_Simulasi_Tata_Surya/**
    - [ ] simulasi_tata_surya.py
    - [ ] visualisasi_orbit.py
    - [ ] **📁 hasil/**
  - [ ] **📁 02_Distribusi_Temperatur_Pelat_Logam/**
    - [ ] heat_equation_2d.py
    - [ ] visualisasi_heatmap.py
    - [ ] **📁 hasil/**
  - [ ] **📁 03_Model_Ising_2D/**
    - [ ] analisis_magnetisasi.py
    - [ ] model_ising_2d.py
    - [ ] **📁 hasil/**
  - [ ] **📁 04_Simulasi_Gelombang_1D_2D/**
    - [ ] animasi_gelombang.py
    - [ ] gelombang_1d.py
    - [ ] gelombang_2d.py
    - [ ] **📁 hasil/**
  - [ ] **📁 05_Model_Penyebaran_Polutan/**
    - [ ] advection_diffusion_pollutant.py
    - [ ] visualisasi_peta_polutan.py
    - [ ] **📁 hasil/**
  - [ ] **📁 06_Optimisasi_Panel_Surya/**
    - [ ] model_radiasi_matahari.py
    - [ ] optimisasi_sudut_panel.py
    - [ ] **📁 hasil/**
  - [ ] **📁 07_Simulasi_Pendulum_Ganda/**
    - [ ] animasi_pendulum.py
    - [ ] pendulum_ganda.py
    - [ ] **📁 hasil/**
- [ ] **📁 05_Topik_Advanced/**
  - [ ] **📁 01_Finite_Difference_Method/**
    - [ ] **📁 Python/**
      - [ ] fdm_laplace_2d.py
      - [ ] fdm_panas_1d.py
      - [ ] fdm_wave_1d.py
  - [ ] **📁 02_Finite_Element_Method/**
    - [ ] **📁 Python/**
      - [ ] fem_1d_poisson.py
      - [ ] fem_beam_sederhana.py
  - [ ] **📁 03_Finite_Volume_Method/**
    - [ ] **📁 Python/**
      - [ ] fvm_advection_1d.py
      - [ ] fvm_diffusion_1d.py
  - [ ] **📁 04_Lattice_Boltzmann_Method/**
    - [ ] **📁 Python/**
      - [ ] lbm_cavity_flow_2d.py
  - [ ] **📁 05_Molecular_Dynamics/**
    - [ ] **📁 Python/**
      - [ ] lennard_jones.py
      - [ ] molecular_dynamics_2d.py
  - [ ] **📁 06_FDTD_Elektromagnetik/**
    - [ ] **📁 Python/**
      - [ ] fdtd_1d.py
      - [ ] fdtd_2d.py
  - [ ] **📁 07_Machine_Learning_for_Physics/**
    - [ ] **📁 Python/**
      - [ ] neural_network_osilator.py
      - [ ] physics_informed_neural_network_pinn.py
      - [ ] regresi_data_fisika.py
- [ ] **📁 06_Notebooks/**
  - [ ] 01_demo_metode_numerik.ipynb
  - [ ] 02_demo_osilator_harmonik.ipynb
  - [ ] 03_demo_persamaan_panas.ipynb
  - [ ] 04_demo_model_ising.ipynb
  - [ ] 05_demo_visualisasi_fisika.ipynb
- [ ] **📁 07_Dataset/**
  - [ ] data_intensitas_cahaya.csv
  - [ ] data_osilator.csv
  - [ ] data_panel_surya.csv
  - [ ] data_suhu_harian.csv
- [ ] **📁 08_Dokumentasi/**
  - [ ] daftar_aplikasi_fisika.md
  - [ ] daftar_metode.md
  - [ ] panduan_penamaan_file.md
  - [ ] referensi_buku_dan_paper.md
  - [ ] roadmap.md
