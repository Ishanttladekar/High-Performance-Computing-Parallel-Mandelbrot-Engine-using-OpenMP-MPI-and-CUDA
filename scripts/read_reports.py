import pypdf
import os

def read_pdf(file_path):
    print(f"=== Reading {file_path} ===")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    reader = pypdf.PdfReader(file_path)
    print(f"Total pages: {len(reader.pages)}")
    for i, page in enumerate(reader.pages):
        print(f"--- Page {i+1} ---")
        text = page.extract_text()
        print(text[:1000]) # first 1000 chars of each page
        print("...")

read_pdf(r"Final_project/Mandelbrot_project.pdf")
