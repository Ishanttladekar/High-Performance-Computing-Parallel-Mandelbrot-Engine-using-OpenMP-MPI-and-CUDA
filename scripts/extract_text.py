import pypdf

reader = pypdf.PdfReader(r"Final_project/Mandelbrot_project.pdf")
with open("mandelbrot_report_text.txt", "w", encoding="utf-8") as f:
    for i, p in enumerate(reader.pages):
        f.write(f"\n\n==================== PAGE {i+1} ====================\n\n")
        f.write(p.extract_text() or "")

print("Extracted", len(reader.pages), "pages.")
