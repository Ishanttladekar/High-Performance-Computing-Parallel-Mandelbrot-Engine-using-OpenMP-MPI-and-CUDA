import urllib.request
import zipfile
import os
import sys

url = "https://github.com/skeeto/w64devkit/releases/download/v1.23.0/w64devkit-1.23.0.zip"
zip_path = r"D:\w64devkit.zip"
extract_dir = r"D:\w64devkit"

if not os.path.exists(extract_dir):
    print("Downloading w64devkit...")
    urllib.request.urlretrieve(url, zip_path)
    print("Downloaded. Extracting...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(r"D:\ ")
    print("Extracted successfully!")
    if os.path.exists(zip_path):
        os.remove(zip_path)
else:
    print("Already exists.")

gpp = r"D:\w64devkit\bin\g++.exe"
print("g++ exists:", os.path.exists(gpp))
