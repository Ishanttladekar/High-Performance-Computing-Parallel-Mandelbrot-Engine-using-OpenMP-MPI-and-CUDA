import os
import subprocess

gcc = r"C:\Users\Dell\w64devkit\bin\gcc.exe"
env = os.environ.copy()
env["PATH"] = r"C:\Users\Dell\w64devkit\bin;" + env["PATH"]

src = r"Assignments\OMP\omp_homework.c"
exe = r"omp_dft.exe"

print("Compiling DFT OpenMP assignment...")
res = subprocess.run([gcc, "-fopenmp", "-O3", src, "-o", exe, "-lm"], env=env, capture_output=True, text=True)
print("Compile exit:", res.returncode)
print("Compile stderr:\n", res.stderr)

if res.returncode == 0:
    print("Running DFT with 4 threads...")
    env["OMP_NUM_THREADS"] = "4"
    res_run = subprocess.run([os.path.abspath(exe)], env=env, capture_output=True, text=True)
    print("Run exit:", res_run.returncode)
    print("Run stdout:\n", res_run.stdout)
