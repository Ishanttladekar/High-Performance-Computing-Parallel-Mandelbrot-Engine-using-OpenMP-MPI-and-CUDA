import zipfile
import os

zip_path = r"D:\w64devkit.zip"
target_dir = r"C:\Users\Dell"

print("Extracting to", target_dir)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(target_dir)

print("Done extraction!")
gpp = r"C:\Users\Dell\w64devkit\bin\g++.exe"
print("g++ exists:", os.path.exists(gpp))
if os.path.exists(zip_path):
    os.remove(zip_path)
