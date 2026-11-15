import numpy as np
import matplotlib.pyplot as plt

print("Loading CSV matrix...")
data = np.loadtxt("mandelbrot_out.csv", delimiter=",", dtype=np.int32)
print("Matrix shape:", data.shape)

plt.figure(figsize=(12, 8), dpi=300)
# Use 'inferno' or 'twilight_shifted' colormap which looks gorgeous for Mandelbrot
plt.imshow(data, cmap='twilight_shifted', extent=[-2, 1, -1, 1])
plt.colorbar(label='Iteration Count')
plt.title('Mandelbrot Set Fractal (Generated via OpenMP Parallelization)')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.tight_layout()
plt.savefig("mandelbrot_fractal.png", dpi=300)
print("Saved mandelbrot_fractal.png successfully!")
