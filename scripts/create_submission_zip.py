import os
import zipfile

zip_filename = "Group_04.zip"

include_dirs = [
    "Assignments",
    "Final_project",
    "Test_scripts",
    "screenshots",
    "report_figures"
]

include_files = [
    "README.md",
    "PROJECT_REPORT.md",
    "PROJECT_REPORT.docx",
    "mandelbrot_fractal.png"
]

print(f"Creating submission archive: {zip_filename} ...")
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
    # Add files
    for f in include_files:
        if os.path.exists(f):
            zf.write(f, arcname=f)
            print(f"Added file: {f}")
        else:
            print(f"Warning: {f} not found!")

    # Add directories
    for d in include_dirs:
        if os.path.exists(d):
            for root, dirs, files in os.walk(d):
                # skip git or cache
                if ".git" in root or "__pycache__" in root:
                    continue
                for file in files:
                    # skip .exe or .o or .log
                    if file.endswith((".exe", ".o", ".obj", ".log", ".tmp")):
                        continue
                    full_p = os.path.join(root, file)
                    rel_p = os.path.relpath(full_p, ".")
                    zf.write(full_p, arcname=rel_p)
            print(f"Added directory: {d}")

print(f"\nDone! Submission ZIP created: {zip_filename}")
print(f"File size: {os.path.getsize(zip_filename):,} bytes ({os.path.getsize(zip_filename)/(1024*1024):.2f} MB)")
