import os
import shutil

os.makedirs("report_figures", exist_ok=True)

mapping = {
    "extracted_figures/p4_2_Im2.png": "report_figures/fig01_mandelbrot_fractal_set.png",
    "extracted_figures/p10_3_Im3.png": "report_figures/fig02_omp_static_exec_time.png",
    "extracted_figures/p12_4_Im4.png": "report_figures/fig03_omp_dynamic_exec_time.png",
    "extracted_figures/p12_5_Im5.png": "report_figures/fig04_omp_parallel_fraction.png",
    "extracted_figures/p13_6_Im6.png": "report_figures/fig05_omp_speedup_static.png",
    "extracted_figures/p13_7_Im7.png": "report_figures/fig06_omp_speedup_dynamic.png",
    "extracted_figures/p14_8_Im8.png": "report_figures/fig07_omp_efficiency_static.png",
    "extracted_figures/p14_9_Im9.png": "report_figures/fig08_omp_efficiency_dynamic.png",
    "extracted_figures/p17_10_Im10.png": "report_figures/fig09_mpi_exec_time_res360.png",
    "extracted_figures/p17_11_Im11.png": "report_figures/fig10_mpi_exec_time_res720.png",
    "extracted_figures/p17_12_Im12.png": "report_figures/fig11_mpi_exec_time_res1000.png",
    "extracted_figures/p18_14_Im14.png": "report_figures/fig12_mpi_speedup.png",
    "extracted_figures/p18_15_Im15.png": "report_figures/fig13_mpi_efficiency.png",
    "extracted_figures/p21_28_Im28.png": "report_figures/fig14_hybrid_bash_script.png",
    "extracted_figures/p22_30_Im30.png": "report_figures/fig15_hybrid_3d_speedup_res360.png",
    "extracted_figures/p23_34_Im34.png": "report_figures/fig16_hybrid_3d_speedup_res1000.png",
    "extracted_figures/p30_41_Im41.png": "report_figures/fig17_cuda_exec_time.png",
    "extracted_figures/p30_42_Im42.png": "report_figures/fig18_cuda_speedup.png",
    "extracted_figures/p31_43_Im43.png": "report_figures/fig19_cuda_efficiency.png",
    "extracted_figures/p32_44_Im44.png": "report_figures/fig20_cross_paradigm_comparison.png",
    "mandelbrot_fractal.png": "screenshots/09_mandelbrot_rendered_fractal.png"
}

for src, dst in mapping.items():
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {src} -> {dst}")
    else:
        print(f"Not found: {src}")

print("Figures organized.")
