# %%
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
# %%
x = np.loadtxt('dir1/x.txt')
y = np.loadtxt('dir2/y.txt')

plt.plot(x, y, "o-", color="magenta", label='Data points')
plt.plot(2*y, .5*x, 'o', color = 'orange')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("What a nice plot! This is so awesome!")
plt.legend()


plot_dir = Path("plots")
plot_dir.mkdir(exist_ok=True)
plt.savefig(plot_dir / "my_plot.png")

