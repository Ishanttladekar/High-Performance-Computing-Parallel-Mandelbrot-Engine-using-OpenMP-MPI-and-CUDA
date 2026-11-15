import pypdf
import os

reader = pypdf.PdfReader(r"Final_project/Mandelbrot_project.pdf")
os.makedirs("extracted_figures", exist_ok=True)

img_count = 0
for i, page in enumerate(reader.pages):
    for img_name, img_obj in page.images.items():
        img_count += 1
        ext = img_obj.name.split(".")[-1]
        out_path = os.path.join("extracted_figures", f"p{i+1}_{img_count}_{img_obj.name}")
        with open(out_path, "wb") as f:
            f.write(img_obj.data)
        print(f"Page {i+1}: extracted {out_path}")

print(f"Total extracted: {img_count}")
