import os
import subprocess
import time

gpp = r"C:\Users\Dell\w64devkit\bin\g++.exe"
env = os.environ.copy()
env["PATH"] = r"C:\Users\Dell\w64devkit\bin;" + env["PATH"]

# Let's create two versions of progetto_omp: static and dynamic
src_code = open(r"Final_project\1_OMP\progetto_omp.cpp", "r").read()

# Dynamic version
src_dynamic = src_code.replace("//#pragma omp parallel for", "//#pragma omp parallel for").replace("#pragma omp parallel for schedule(dynamic)", "#pragma omp parallel for schedule(dynamic)")
with open("omp_dynamic.cpp", "w") as f:
    f.write(src_dynamic)

# Static version
src_static = src_code.replace("#pragma omp parallel for schedule(dynamic)", "#pragma omp parallel for schedule(static)")
with open("omp_static.cpp", "w") as f:
    f.write(src_static)

# Compile both
print("Compiling omp_dynamic...")
subprocess.run([gpp, "-fopenmp", "-O3", "omp_dynamic.cpp", "-o", "omp_dynamic.exe"], env=env, check=True)
print("Compiling omp_static...")
subprocess.run([gpp, "-fopenmp", "-O3", "omp_static.cpp", "-o", "omp_static.exe"], env=env, check=True)

threads_list = [1, 2, 4, 8]
results_dynamic = {}
results_static = {}

print("\n--- BENCHMARKING DYNAMIC SCHEDULING ---")
for t in threads_list:
    env["OMP_NUM_THREADS"] = str(t)
    # run 2 times and take average
    times = []
    for rep in range(2):
        res = subprocess.run(["omp_dynamic.exe", "test.csv"], env=env, capture_output=True, text=True)
        # Parse: Elapsed time (s) = X.XXXXXX
        for line in res.stdout.split("\n"):
            if "Elapsed time" in line:
                val = float(line.split("=")[1].strip())
                times.append(val)
    avg_t = sum(times) / len(times)
    results_dynamic[t] = avg_t
    print(f"Threads: {t} -> Time: {avg_t:.4f} s")

print("\n--- BENCHMARKING STATIC SCHEDULING ---")
for t in threads_list:
    env["OMP_NUM_THREADS"] = str(t)
    times = []
    for rep in range(2):
        res = subprocess.run(["omp_static.exe", "test.csv"], env=env, capture_output=True, text=True)
        for line in res.stdout.split("\n"):
            if "Elapsed time" in line:
                val = float(line.split("=")[1].strip())
                times.append(val)
    avg_t = sum(times) / len(times)
    results_static[t] = avg_t
    print(f"Threads: {t} -> Time: {avg_t:.4f} s")

print("\n=== SUMMARY RESULTS ===")
print("Threads | Static (s) | Dynamic (s) | Speedup (Dynamic)")
t1 = results_dynamic[1]
for t in threads_list:
    st = results_static[t]
    dt = results_dynamic[t]
    sp = t1 / dt
    print(f"{t:7d} | {st:10.4f} | {dt:11.4f} | {sp:17.2f}x")

if os.path.exists("test.csv"):
    os.remove("test.csv")
