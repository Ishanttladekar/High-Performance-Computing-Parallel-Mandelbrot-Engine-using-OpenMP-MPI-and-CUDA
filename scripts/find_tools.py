import os

search_dirs = [
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    r"C:\msys64",
    r"C:\tools",
    r"C:\Users\Dell\AppData\Local",
    r"C:\cygwin64",
    r"C:\Program Files\NVIDIA GPU Computing Toolkit",
    r"C:\Program Files (x86)\Microsoft SDKs\MPI",
    r"C:\Program Files\Microsoft MPI",
]

found = []
for d in search_dirs:
    if os.path.exists(d):
        print(f"Exists: {d}")
        for root, dirs, files in os.walk(d):
            # don't go too deep
            depth = root[len(d):].count(os.sep)
            if depth > 3:
                dirs.clear()
                continue
            for f in files:
                f_lower = f.lower()
                if f_lower in ["gcc.exe", "g++.exe", "clang.exe", "cl.exe", "nvcc.exe", "mpicc.exe", "mpiexec.exe"]:
                    found.append(os.path.join(root, f))
    else:
        pass

print("Found compilers/tools:")
for item in found:
    print(item)
