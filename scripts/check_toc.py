with open("mandelbrot_report_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect TOC and headings
lines = text.split("\n")
for line in lines:
    if line.startswith("===") or line.strip().startswith("1 ") or line.strip().startswith("2 ") or line.strip().startswith("3 ") or line.strip().startswith("4 ") or line.strip().startswith("5 ") or line.strip().startswith("6 ") or line.strip().startswith("7 ") or "Table" in line or "Figure" in line:
        print(line[:120])
