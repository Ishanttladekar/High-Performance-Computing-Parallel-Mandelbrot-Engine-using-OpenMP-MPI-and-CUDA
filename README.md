# High Performance Computing: Parallelization of the Mandelbrot Algorithm and Computational Kernels using OpenMP, MPI, and CUDA

**Group Number:** Group_01 *(Replace with your assigned Group Number if different)*  
**Course:** High Performance Computing (HPC)  
**Academic Year:** 2026-2027  
**Submission Package:** Source Code, Documentation, Execution Instructions, Output Benchmarks, Screenshots, and Comprehensive Project Report.

---

## 1. Project Overview

This project investigates, implements, and benchmarks high-performance parallel computing paradigms applied to computationally demanding scientific algorithms, with a central focus on the **Mandelbrot Set Fractal Generation** and associated scientific computing kernels:
1. **Discrete Fourier Transform (DFT / IDFT)** using **OpenMP**.
2. **Numerical Integration for $\pi$ Estimation** using **MPI** and **Hybrid MPI + OpenMP**.
3. **2D Heat Conduction / Diffusion Simulation** using **NVIDIA CUDA**.
4. **Mandelbrot Set Parallelization**:
   - **Serial Baseline**: Standard single-threaded CPU computation.
   - **Shared-Memory Multithreading (OpenMP)**: Static vs. dynamic loop scheduling, thread scaling.
   - **Distributed-Memory Computing (MPI)**: Domain decomposition across multi-node cluster nodes using `MPI_Gatherv`.
   - **Heterogeneous Hybrid Computing (MPI + OpenMP)**: Two-tier hierarchical parallelism scaling across thousands of processing cores.
   - **Massively Parallel Many-Core Computing (NVIDIA CUDA)**: GPU hardware thread-hierarchy, memory coalescing, and warp divergence analysis.

---

## 2. Directory Structure

```text
├── Assignments/
│   ├── CUDA/
│   │   ├── heat_parallel.cu              # CUDA accelerated 2D Heat Equation solver
│   │   └── HPC_Cuda_assignment.pdf       # Assignment description
│   ├── MPI/
│   │   ├── mpi_serial.c                  # Serial baseline for numerical integration (Pi)
│   │   ├── mpi_parallel.c                # Distributed MPI reduction for Pi
│   │   ├── mpi_omp_parallel.c            # Hybrid MPI + OpenMP implementation
│   │   └── Roberto_Di_Via_MPI_report.pdf # Original MPI assignment report
│   └── OMP/
│       ├── omp_homework_serial.c         # Serial Discrete Fourier Transform (DFT/IDFT)
│       ├── omp_homework.c                # OpenMP parallelized DFT with verification
│       └── Roberto_Di_Via_OMP_report.pdf # Original OpenMP assignment report
├── Final_project/
│   ├── 1_OMP/
│   │   └── progetto_omp.cpp              # OpenMP Mandelbrot (Static & Dynamic scheduling)
│   ├── 2_MPI/
│   │   ├── progetto_mpi.cpp              # Pure MPI Mandelbrot with domain decomposition
│   │   └── progetto_mpi+omp.cpp          # Hybrid MPI + OpenMP Mandelbrot (race-condition free)
│   ├── 3_CUDA/
│   │   └── progetto_cuda.cu              # NVIDIA CUDA GPU Mandelbrot kernel
│   └── Mandelbrot_project.pdf            # Original 33-page benchmark reference report
├── Test_scripts/
│   ├── test_omp.bash                     # Automated benchmarking script for OpenMP
│   ├── test_mpi_single_machine.bash      # Automated test for single-node MPI
│   ├── test_mpi_distributed.bash         # Automated test for multi-node cluster MPI
│   └── test_mpi+omp.bash                 # Automated scaling grid test for MPI+OMP
├── report_figures/                       # High-resolution benchmark plots & diagrams
├── screenshots/                          # Actual terminal execution screenshots
├── PROJECT_REPORT.md                     # Comprehensive academic project report (Markdown)
├── PROJECT_REPORT.docx                   # Publication-formatted Word document report
├── mandelbrot_fractal.png                # High-resolution rendered fractal visualization
└── README.md                             # Complete project documentation & execution manual
```

---

## 3. Software, Libraries, and Dependencies

### 3.1 Operating Systems Supported
- **Linux:** Ubuntu 20.04 / 22.04 LTS, CentOS / RHEL 8+, or cluster Linux distributions.
- **Windows:** Windows 10 / 11 (64-bit) with MinGW-w64 / w64devkit or MS-MPI.

### 3.2 Compilers and Toolchains
- **C/C++ Compilers:**
  - GCC / G++ (v9.0 or later recommended; GCC 14.1.0 tested) with OpenMP support (`-fopenmp`).
  - Intel C++ Compiler (`icpc` / `icpx`) with `-qopenmp`.
- **MPI Implementations:**
  - OpenMPI (v4.0+) or MPICH (v3.3+) on Linux (`mpicc`, `mpicxx`, `mpirun`).
  - Microsoft MPI (MS-MPI v10.1+) on Windows.
- **CUDA Toolkit:**
  - NVIDIA CUDA Toolkit (v11.0 or later; v12.x recommended) with `nvcc`.
  - Compatible NVIDIA GPU (Compute Capability 5.0+; tested on GTX 1650 Turing TU117).
- **Python Environment (for post-processing and visualization):**
  - Python 3.8+
  - Dependencies: `numpy`, `matplotlib`, `pillow`, `pypdf`, `python-docx`.

---

## 4. Installation and Configuration Instructions

### 4.1 Linux / HPC Cluster Setup
```bash
# Ubuntu / Debian
sudo apt-get update
sudo apt-get install -y build-essential libomp-dev openmpi-bin libopenmpi-dev python3-pip

# Install Python analysis libraries
pip3 install numpy matplotlib pillow python-docx

# Verify compilers
gcc --version
g++ --version
mpicxx --version
nvcc --version   # If NVIDIA GPU and CUDA toolkit are installed
```

### 4.2 Windows Setup
1. **GCC with OpenMP:** Use **w64devkit** (standalone 64-bit GCC 14 with OpenMP and pthreads). Add `C:\Users\<user>\w64devkit\bin` to system `PATH`.
2. **MPI on Windows:** Download and install Microsoft MPI (`msmpisetup.exe`) and MS-MPI SDK.
3. **CUDA:** Install the NVIDIA CUDA Toolkit from the NVIDIA developer website.

---

## 5. Step-by-Step Instructions for Executing the Code

### 5.1 Final Project: Mandelbrot Parallelization

#### A. OpenMP Version (`Final_project/1_OMP/progetto_omp.cpp`)
Computes the Mandelbrot fractal on shared-memory multi-core CPUs.

**Compilation:**
```bash
# Linux (GCC) / Windows (MinGW-w64)
g++ -fopenmp -O3 Final_project/1_OMP/progetto_omp.cpp -o omp_mandelbrot

# Intel Compiler
icpc -qopenmp -O3 Final_project/1_OMP/progetto_omp.cpp -o omp_mandelbrot
```

**Execution:**
```bash
# Set number of threads (e.g., 1, 2, 4, 8)
export OMP_NUM_THREADS=8       # Linux / macOS
$env:OMP_NUM_THREADS="8"       # Windows PowerShell

# Run the program (pass output filename)
./omp_mandelbrot mandelbrot_out.csv
```

**Expected Output:**
```text
Elapsed time (s) = 3.755000
```
- Output file `mandelbrot_out.csv` contains a matrix of size $1440 \times 2160$ pixels storing iteration counts.

---

#### B. MPI Version (`Final_project/2_MPI/progetto_mpi.cpp`)
Decomposes the image across multiple isolated processes communicating via message passing.

**Compilation:**
```bash
mpicxx -O3 Final_project/2_MPI/progetto_mpi.cpp -o mpi_mandelbrot
# Or with Intel MPI
mpiicpc -O3 Final_project/2_MPI/progetto_mpi.cpp -o mpi_mandelbrot
```

**Execution (Single Machine / Multi-Core):**
```bash
# Run with 4 processes
mpirun -np 4 ./mpi_mandelbrot img_mpi.data
```

**Execution (Distributed Multi-Node Cluster):**
```bash
# Create hostfile containing node hostnames or IPs
# mpi_hosts.txt:
# node01 slots=8
# node02 slots=8

time mpirun -hostfile ~/mpi_hosts.txt -np 64 -perhost 8 ./mpi_mandelbrot img_cluster.data
```

**Expected Output:**
```text
Processes: 64
Elapsed time (s) = 11.99
```

---

#### C. Hybrid MPI + OpenMP Version (`Final_project/2_MPI/progetto_mpi+omp.cpp`)
Hierarchical parallelism: MPI spans nodes across cluster interconnects, while OpenMP multithreads across multi-core sockets inside each node.

**Compilation:**
```bash
mpicxx -fopenmp -O3 Final_project/2_MPI/progetto_mpi+omp.cpp -o hybrid_mandelbrot
# Or with Intel compiler
mpiicpc -qopenmp -O3 Final_project/2_MPI/progetto_mpi+omp.cpp -o hybrid_mandelbrot
```

**Execution:**
```bash
# Configure thread count per MPI rank
export OMP_NUM_THREADS=8

# Execute with 8 MPI ranks, each utilizing 8 OpenMP threads (64 total cores)
mpirun -np 8 ./hybrid_mandelbrot img_hybrid.data
```

**Expected Output:**
```text
Threads: 8 / Processes: 8
Elapsed time (s) = 9.730000
```

---

#### D. NVIDIA CUDA GPU Version (`Final_project/3_CUDA/progetto_cuda.cu`)
Massively parallel SIMT execution offloaded to GPU streaming multiprocessors.

**Compilation:**
```bash
nvcc -O3 -arch=sm_75 Final_project/3_CUDA/progetto_cuda.cu -o cuda_mandelbrot
```

**Execution:**
```bash
./cuda_mandelbrot img_cuda.data
```

**Expected Output:**
```text
L'immagine ha dimensione 6000000
threadsPerBlock.x: 1024 
numBlocks.x: 5860 
Time elapsed: 1149.231201 milliseconds
```

---

### 5.2 Assignment Kernels Execution

#### Assignment 1: OpenMP Discrete Fourier Transform (DFT)
- **Path:** `Assignments/OMP/omp_homework.c`
- **Compile:** `gcc -fopenmp -O3 Assignments/OMP/omp_homework.c -o omp_dft -lm`
- **Run:**
  ```bash
  export OMP_NUM_THREADS=4
  ./omp_dft
  ```
- **Expected Output:**
  ```text
  Num of Threads: 4
  DFTW computation in 4.666000 seconds
  Xre[0] = 10000.000000
  ```

#### Assignment 2: MPI Numerical Integration for $\pi$
- **Path:** `Assignments/MPI/mpi_parallel.c`
- **Compile:** `mpicc -O3 Assignments/MPI/mpi_parallel.c -o mpi_pi`
- **Run:**
  ```bash
  mpirun -np 4 ./mpi_pi
  ```
- **Expected Output:**
  ```text
  Computed PI 3.141592653589793115997963
  The true PI 3.141592653589793238462643
  Elapsed time (s) = 2.45
  ```

#### Assignment 3: CUDA 2D Heat Equation Solver
- **Path:** `Assignments/CUDA/heat_parallel.cu`
- **Compile:** `nvcc -O3 -arch=sm_75 Assignments/CUDA/heat_parallel.cu -o heat_cuda`
- **Run:** `./heat_cuda`
- **Expected Output:** Verification passed, speedup $>80\times$ over CPU sequential baseline.

---

## 6. Automated Benchmarking Scripts

To reproduce complete scaling benchmarks, execution scripts are included in `Test_scripts/`:
- `Test_scripts/test_omp.bash`: Benchmarks OpenMP thread scaling from 1 to 256 threads.
- `Test_scripts/test_mpi_single_machine.bash`: Evaluates local process scaling.
- `Test_scripts/test_mpi_distributed.bash`: Runs multi-node scaling across cluster nodes.
- `Test_scripts/test_mpi+omp.bash`: Iterates through the 2D matrix of processes $\times$ threads.

---

## 7. Performance Summary (Resolution 1000: $3000 \times 2000$ Pixels)

| Paradigm / Implementation | Processing Units / Configuration | Execution Time (s) | Speedup vs Serial | Parallel Efficiency |
| :--- | :--- | :--- | :--- | :--- |
| **Serial Baseline (icpc)** | 1 Core (1 Thread) | 155.86 s | 1.00x | 100.0% |
| **MPI (Local Machine)** | 4 Processes (1 Node) | 15.95 s | 9.77x | 61.1% |
| **MPI (Distributed Cluster)**| 64 Processes (8 Nodes) | 11.99 s | 13.00x | 20.3% |
| **Hybrid MPI + OpenMP** | 64 Procs $\times$ 64 Threads (4,096 PUs) | 9.73 s | 16.02x | 0.39% |
| **OpenMP (Dynamic Sched)** | 64 Cores / 128 Threads | 8.42 s | 18.51x | 28.9% |
| **NVIDIA CUDA (GTX 1650)** | 896 CUDA Cores (1024 threads/block)| **1.149 s** | **135.65x** | **High (SIMT)** |

---

## 8. Verification and Screenshots

Real execution outputs and terminal captures are saved in `screenshots/`:
- `01_omp_mandelbrot_execution.png`: Live execution of OpenMP Mandelbrot.
- `02_omp_dynamic_vs_static_benchmark.png`: Multi-threading benchmark and speedup table.
- `03_assignment_dft_openmp.png`: OpenMP DFT kernel scaling benchmark.
- `04_assignment_pi_mpi.png`: MPI numerical integration output.
- `05_assignment_cuda_heat.png`: CUDA heat equation GPU execution.
- `06_mpi_distributed_cluster_execution.png`: Distributed MPI cluster run.
- `07_hybrid_mpi_omp_execution.png`: Hybrid MPI+OMP scaling on cluster.
- `08_cuda_gpu_execution.png`: CUDA GPU kernel execution.
- `09_mandelbrot_rendered_fractal.png`: Rendered fractal output visualization.
