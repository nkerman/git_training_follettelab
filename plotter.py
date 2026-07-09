# %%
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
# %%
x = np.loadtxt('dir1/x.txt')
y = np.loadtxt('dir2/y.txt')
plt.plot(x, y, "o-")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("What a nice plot! This is so awesome!")

plot_dir = Path("plots")
plot_dir.mkdir(exist_ok=True)
plt.savefig(plot_dir / "my_plot.png")
