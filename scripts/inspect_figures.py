import os
from PIL import Image

for f in sorted(os.listdir("extracted_figures")):
    p = os.path.join("extracted_figures", f)
    try:
        im = Image.open(p)
        print(f"{f}: {im.size} {im.format} {im.mode}")
    except Exception as e:
        print(f"{f}: error {e}")
