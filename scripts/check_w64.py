import os

base = r"C:\Users\Dell\w64devkit"
for root, dirs, files in os.walk(base):
    for f in files:
        if f.startswith("cc1") or f == "as.exe":
            print(os.path.join(root, f))
