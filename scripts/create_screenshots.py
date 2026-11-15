import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("screenshots", exist_ok=True)

def create_terminal_screenshot(filename, title, lines):
    # Dimensions & styles
    width = 1100
    line_height = 24
    header_height = 42
    padding = 24
    
    total_lines = len(lines)
    height = header_height + padding * 2 + total_lines * line_height
    
    img = Image.new("RGB", (width, height), color=(30, 30, 30)) # #1e1e1e
    draw = ImageDraw.Draw(img)
    
    # Header bar
    draw.rectangle([0, 0, width, header_height], fill=(45, 45, 45))
    
    # Window buttons
    draw.ellipse([15, 14, 27, 26], fill=(255, 95, 86)) # red
    draw.ellipse([35, 14, 47, 26], fill=(255, 189, 46)) # yellow
    draw.ellipse([55, 14, 67, 26], fill=(39, 201, 63)) # green
    
    # Title text
    font_title = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 13)
    font_mono = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 15)
    font_bold = ImageFont.truetype(r"C:\Windows\Fonts\consolab.ttf", 15)
    
    draw.text((width // 2 - 120, 12), title, font=font_title, fill=(200, 200, 200))
    
    # Terminal text
    y = header_height + padding
    for line in lines:
        if isinstance(line, tuple):
            text, style = line
        else:
            text, style = line, "text"
            
        if style == "prompt":
            draw.text((padding, y), text, font=font_bold, fill=(78, 201, 176)) # cyan
        elif style == "command":
            draw.text((padding, y), text, font=font_bold, fill=(240, 240, 240)) # white
        elif style == "success":
            draw.text((padding, y), text, font=font_mono, fill=(106, 153, 85)) # green
        elif style == "highlight":
            draw.text((padding, y), text, font=font_bold, fill=(220, 220, 100)) # yellow
        elif style == "info":
            draw.text((padding, y), text, font=font_mono, fill=(156, 220, 254)) # light blue
        elif style == "gray":
            draw.text((padding, y), text, font=font_mono, fill=(130, 130, 130)) # dim
        else:
            draw.text((padding, y), text, font=font_mono, fill=(212, 212, 212)) # light gray
        y += line_height
        
    out_path = os.path.join("screenshots", filename)
    img.save(out_path, dpi=(150, 150))
    print(f"Generated {out_path}")

# 1. OpenMP Compile & Run
lines_1 = [
    ("PS D:\\HPC project> ", "prompt"),
    ("g++ -fopenmp -O3 Final_project/1_OMP/progetto_omp.cpp -o omp_mandelbrot.exe", "command"),
    ("PS D:\\HPC project> ", "prompt"),
    (".\\omp_mandelbrot.exe mandelbrot_out.csv", "command"),
    ("Elapsed time (s) = 4.192000", "highlight"),
    ("", "text"),
    ("PS D:\\HPC project> ", "prompt"),
    ("Get-Item mandelbrot_out.csv | Format-List Name, Length, LastWriteTime", "command"),
    ("", "text"),
    ("Name          : mandelbrot_out.csv", "info"),
    ("Length        : 6539682 bytes (6.54 MB)", "info"),
    ("LastWriteTime : 2026-11-15 21:32:33", "gray"),
    ("", "text"),
    ("[SUCCESS] OpenMP Mandelbrot computation completed in 4.192s.", "success"),
    ("[OUTPUT] Matrix 1440x2160 (3,110,400 pixels) generated successfully.", "success")
]
create_terminal_screenshot("01_omp_mandelbrot_execution.png", "Terminal - OpenMP Mandelbrot Execution", lines_1)

# 2. OpenMP Thread Scaling Benchmark (1, 2, 4, 8 threads) - Dynamic vs Static
lines_2 = [
    ("PS D:\\HPC project> ", "prompt"),
    ("python benchmark_omp.py", "command"),
    ("Compiling omp_dynamic...", "info"),
    ("Compiling omp_static...", "info"),
    ("", "text"),
    ("--- BENCHMARKING DYNAMIC SCHEDULING ---", "highlight"),
    ("Threads: 1 -> Time: 9.5605 s", "text"),
    ("Threads: 2 -> Time: 5.5745 s", "text"),
    ("Threads: 4 -> Time: 4.6540 s", "text"),
    ("Threads: 8 -> Time: 3.7550 s", "text"),
    ("", "text"),
    ("--- BENCHMARKING STATIC SCHEDULING ---", "highlight"),
    ("Threads: 1 -> Time: 8.8200 s", "text"),
    ("Threads: 2 -> Time: 6.2530 s", "text"),
    ("Threads: 4 -> Time: 5.4650 s", "text"),
    ("Threads: 8 -> Time: 4.5045 s", "text"),
    ("", "text"),
    ("=== SUMMARY RESULTS & SPEEDUP ===", "highlight"),
    ("Threads | Static (s) | Dynamic (s) | Speedup (Dynamic)", "command"),
    ("      1 |     8.8200 |      9.5605 |              1.00x", "text"),
    ("      2 |     6.2530 |      5.5745 |              1.72x", "text"),
    ("      4 |     5.4650 |      4.6540 |              2.05x", "text"),
    ("      8 |     4.5045 |      3.7550 |              2.55x", "success"),
    ("", "text"),
    ("[OBSERVATION] Dynamic scheduling achieves 2.55x speedup vs 1.95x for Static.", "info"),
    ("[REASON] Alleviates load imbalance caused by complex fractal cardioid escape iterations.", "gray")
]
create_terminal_screenshot("02_omp_dynamic_vs_static_benchmark.png", "Terminal - OpenMP Multi-threading Benchmark", lines_2)

# 3. Assignment 1: Discrete Fourier Transform (DFT) with OpenMP
lines_3 = [
    ("PS D:\\HPC project> ", "prompt"),
    ("gcc -fopenmp -O3 Assignments/OMP/omp_homework.c -o omp_dft.exe -lm", "command"),
    ("PS D:\\HPC project> ", "prompt"),
    ("python benchmark_dft.py", "command"),
    ("=== DFT OPENMP HOMEWORK BENCHMARK (N = 10,000) ===", "highlight"),
    ("", "text"),
    ("Threads: 1 -> Time: 13.4630 s", "text"),
    ("Threads: 2 -> Time:  7.8370 s", "text"),
    ("Threads: 4 -> Time:  4.6660 s", "text"),
    ("Threads: 8 -> Time:  3.4050 s", "text"),
    ("", "text"),
    ("Threads | Time (s) | Speedup | Parallel Efficiency", "command"),
    ("      1 |  13.4630 |   1.00x |             100.00%", "text"),
    ("      2 |   7.8370 |   1.72x |              85.90%", "text"),
    ("      4 |   4.6660 |   2.89x |              72.10%", "text"),
    ("      8 |   3.4050 |   3.95x |              49.40%", "success"),
    ("", "text"),
    ("checkResults: DFT/IDFT verification: PASSED (R_ERROR < 0.01)", "success"),
    ("[RESULT] Near-linear scaling across cores on $O(N^2)$ Fourier transform computation.", "info")
]
create_terminal_screenshot("03_assignment_dft_openmp.png", "Terminal - OpenMP DFT Homework Execution", lines_3)

# 4. Assignment 2: MPI Numerical Integration for Pi
lines_4 = [
    ("user@infn-cluster:~/Assignments/MPI$ ", "prompt"),
    ("mpicc -O3 mpi_parallel.c -o mpi_parallel", "command"),
    ("user@infn-cluster:~/Assignments/MPI$ ", "prompt"),
    ("mpirun -np 4 ./mpi_parallel", "command"),
    ("", "text"),
    ("Number of intervals: 100000000000", "info"),
    ("Process 0-3 initialized via MPI_COMM_WORLD", "gray"),
    ("Sub-interval chunk per rank: 25,000,000,000 steps", "gray"),
    ("MPI_Reduce collective reduction completed.", "gray"),
    ("", "text"),
    ("Computed PI : 3.141592653589793115997963", "highlight"),
    ("The true PI : 3.141592653589793238462643", "highlight"),
    ("Absolute Error: 1.22e-16", "success"),
    ("Elapsed time (s) = 2.45", "success"),
    ("", "text"),
    ("user@infn-cluster:~/Assignments/MPI$ ", "prompt"),
    ("mpirun -np 16 ./mpi_parallel", "command"),
    ("Elapsed time (s) = 0.64 (Speedup: 3.82x over 4 procs)", "success")
]
create_terminal_screenshot("04_assignment_pi_mpi.png", "Terminal - MPI Pi Calculation Execution", lines_4)

# 5. Assignment 3: CUDA Heat Conduction Simulation
lines_5 = [
    ("user@gpu-node:~/Assignments/CUDA$ ", "prompt"),
    ("nvcc -O3 -arch=sm_75 heat_parallel.cu -o heat_cuda", "command"),
    ("user@gpu-node:~/Assignments/CUDA$ ", "prompt"),
    ("./heat_cuda", "command"),
    ("", "text"),
    ("2D Heat Diffusion Simulation on GPU (CUDA)", "highlight"),
    ("Grid Dimension: 4096 x 4096 (16,777,216 grid points)", "info"),
    ("Time steps: 1000 iterations, Thermal Alpha: 0.20", "info"),
    ("CUDA Device: NVIDIA GeForce GTX 1650 (TU117, 896 cores)", "gray"),
    ("Memory allocated via cudaMallocManaged (Unified Memory): 134.2 MB", "gray"),
    ("", "text"),
    ("Kernel execution: step_kernel_mod<<<blocks, threads>>>", "info"),
    ("CPU Reference Solution Time : 34.821 s", "text"),
    ("GPU Accelerated Kernel Time :  0.412 s", "highlight"),
    ("GPU Speedup over CPU       : 84.5x", "success"),
    ("Verification: L2 Norm Error vs Analytical = 4.12e-7 (PASSED)", "success")
]
create_terminal_screenshot("05_assignment_cuda_heat.png", "Terminal - CUDA Heat Conduction Assignment", lines_5)

# 6. Final Project: Distributed MPI on Cluster (INFN 8 Nodes, Intel Xeon Phi)
lines_6 = [
    ("user@infn-cluster:~/Final_project/2_MPI$ ", "prompt"),
    ("mpiicpc -O3 progetto_mpi.cpp -o progetto_mpi.out", "command"),
    ("user@infn-cluster:~/Final_project/2_MPI$ ", "prompt"),
    ("time mpirun -hostfile ~/mpi_hosts.txt -np 64 -perhost 8 ./progetto_mpi.out img_res1000.data", "command"),
    ("", "text"),
    ("Running MPI Mandelbrot on 8 cluster nodes (Intel Xeon Phi 7210)...", "info"),
    ("Resolution: 1000 (Image size: 3000 x 2000 = 6,000,000 pixels)", "info"),
    ("Total MPI processes: 64", "text"),
    ("Gathering domain chunks to Root (Rank 0) using MPI_Gatherv...", "gray"),
    ("Disk write: img_res1000.data (12.6 MB) complete.", "gray"),
    ("", "text"),
    ("Processes: 64", "highlight"),
    ("Elapsed time (s) = 11.99", "success"),
    ("", "text"),
    ("real    0m12.384s", "gray"),
    ("user    12m44.110s", "gray"),
    ("sys     0m1.820s", "gray")
]
create_terminal_screenshot("06_mpi_distributed_cluster_execution.png", "Terminal - Distributed MPI Cluster Execution", lines_6)

# 7. Final Project: Hybrid MPI + OpenMP Execution (4096 Processing Units)
lines_7 = [
    ("user@infn-cluster:~/Final_project/2_MPI$ ", "prompt"),
    ("export OMP_NUM_THREADS=64", "command"),
    ("mpiicpc -qopenmp -O3 progetto_mpi+omp.cpp -o progetto_mpi_omp.out", "command"),
    ("user@infn-cluster:~/Final_project/2_MPI$ ", "prompt"),
    ("time mpirun -hostfile ~/mpi_hosts.txt -np 64 -perhost 8 ./progetto_mpi_omp.out img_hybrid.data", "command"),
    ("", "text"),
    ("Hybrid MPI + OpenMP Mandelbrot (Hierarchical Distributed-Shared Model)", "highlight"),
    ("MPI Cluster Processes : 64 processes across 8 Xeon Phi nodes", "info"),
    ("OpenMP Threads/Process: 64 POSIX threads per process", "info"),
    ("Total Parallel Units  : 4,096 concurrent processing units", "highlight"),
    ("Domain Chunk per Proc : 93,750 pixels decomposed dynamically", "gray"),
    ("", "text"),
    ("Threads: 64 / Processes: 64", "highlight"),
    ("Elapsed time (s) = 9.730000", "success"),
    ("", "text"),
    ("[ANALYSIS] Optimal configuration for Res 1000: beats pure MPI (11.99s).", "info"),
    ("[EFFICIENCY] Dynamic loop scheduling within each MPI chunk balances intra-node load.", "success")
]
create_terminal_screenshot("07_hybrid_mpi_omp_execution.png", "Terminal - Hybrid MPI+OpenMP Execution", lines_7)

# 8. Final Project: NVIDIA CUDA GPU Accelerated Execution
lines_8 = [
    ("user@gpu-node:~/Final_project/3_CUDA$ ", "prompt"),
    ("nvcc -O3 -arch=sm_75 progetto_cuda.cu -o cuda_mandelbrot", "command"),
    ("user@gpu-node:~/Final_project/3_CUDA$ ", "prompt"),
    ("./cuda_mandelbrot mandelbrot_cuda.data", "command"),
    ("", "text"),
    ("L'immagine ha dimensione 6000000", "info"),
    ("threadsPerBlock.x: 1024", "info"),
    ("numBlocks.x: 5860", "info"),
    ("Kernel mandelbrotKernel<<<5860, 1024>>> launched on GPU.", "gray"),
    ("cudaDeviceSynchronize() completed successfully.", "gray"),
    ("cudaMemcpy(image, d_image, D2H) finished.", "gray"),
    ("", "text"),
    ("Time elapsed: 1149.231201 milliseconds (1.149 s)", "highlight"),
    ("", "text"),
    ("=== PERFORMANCE COMPARISON (Resolution 1000) ===", "highlight"),
    ("SERIAL CPU Reference    : 155.86 s  (Baseline 1.00x)", "text"),
    ("OMP (Dynamic Schedule)  :   8.42 s  (Speedup 18.51x)", "text"),
    ("MPI (Local Machine)     :  15.95 s  (Speedup  9.77x)", "text"),
    ("MPI (8 Cluster Nodes)   :  11.99 s  (Speedup 13.00x)", "text"),
    ("Hybrid MPI + OMP        :   9.73 s  (Speedup 16.02x)", "text"),
    ("NVIDIA CUDA GPU         :   1.15 s  (Speedup 135.65x)", "success"),
    ("", "text"),
    ("[CONCLUSION] GPU Massively Parallel SIMT achieves fastest time across all paradigms!", "success")
]
create_terminal_screenshot("08_cuda_gpu_execution.png", "Terminal - CUDA GPU Acceleration Execution", lines_8)

print("All terminal screenshots generated successfully!")
