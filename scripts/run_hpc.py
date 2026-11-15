import os
import subprocess

gpp = r"C:\Users\Dell\w64devkit\bin\g++.exe"
env = os.environ.copy()
env["PATH"] = r"C:\Users\Dell\w64devkit\bin;" + env["PATH"]

src = r"Final_project\1_OMP\progetto_omp.cpp"
exe = r"omp_mandelbrot.exe"

print("Compiling OpenMP code with w64devkit g++...")
cmd_compile = [gpp, "-fopenmp", "-O3", src, "-o", exe]
res = subprocess.run(cmd_compile, env=env, capture_output=True, text=True)
print("Compile exit:", res.returncode)
print("Compile stdout:", res.stdout)
print("Compile stderr:", res.stderr)

if res.returncode == 0:
    print("Compilation succeeded! Running OpenMP Mandelbrot...")
    cmd_run = [os.path.abspath(exe), "mandelbrot_out.csv"]
    res_run = subprocess.run(cmd_run, env=env, capture_output=True, text=True)
    print("Run exit:", res_run.returncode)
    print("Run stdout:\n", res_run.stdout)
    print("Run stderr:\n", res_run.stderr)
