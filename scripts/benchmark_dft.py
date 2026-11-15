import os
import subprocess

gcc = r"C:\Users\Dell\w64devkit\bin\gcc.exe"
env = os.environ.copy()
env["PATH"] = r"C:\Users\Dell\w64devkit\bin;" + env["PATH"]

src = r"Assignments\OMP\omp_homework.c"
exe = r"omp_dft.exe"

subprocess.run([gcc, "-fopenmp", "-O3", src, "-o", exe, "-lm"], env=env, check=True)

print("=== DFT BENCHMARK ===")
threads = [1, 2, 4, 8]
dft_results = {}
for t in threads:
    env["OMP_NUM_THREADS"] = str(t)
    res = subprocess.run([os.path.abspath(exe)], env=env, capture_output=True, text=True)
    for line in res.stdout.split("\n"):
        if "DFTW computation in" in line:
            val = float(line.split("in")[1].split("seconds")[0].strip())
            dft_results[t] = val
            print(f"Threads: {t} -> Time: {val:.4f} s")

t1 = dft_results[1]
print("\nThreads | Time (s) | Speedup")
for t in threads:
    tm = dft_results[t]
    print(f"{t:7d} | {tm:8.4f} | {t1/tm:7.2f}x")
