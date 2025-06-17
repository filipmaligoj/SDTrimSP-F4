# plot_xy_simple.py
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# File path (adjust if necessary)
file_path = Path("/home/sancho/Documents/SDTrimSP/Matjaž Panjan/2025-06-17/Ar-Ti(500eV)(100nm)/Results3/Implantation_depth.txt")

# Load 2-column data, skipping header
data = np.loadtxt(file_path, skiprows=1, usecols=(0, 1))

# Split columns into x and y
x_vals = data[:, 0]
y_vals = data[:, 1]

# Plot
plt.figure(figsize=(7, 5))
plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X vs Y from ion-induced_damages.txt')
plt.grid(True)
plt.tight_layout()
plt.show()
