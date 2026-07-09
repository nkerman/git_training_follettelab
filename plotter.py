# %%
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# %%
x = np.loadtxt('dir1/x.txt')
y = np.loadtxt('dir2/y.txt')

points = np.array([np.linspace(x.min(), x.max()), np.ones(50)]).T.reshape(-1,1,2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
norm = plt.Normalize(x.min(), x.max())
lc = LineCollection(segments, zorder=1, cmap='cool', norm=norm)
lc.set_array(np.linspace(x.min(), x.max()))
lc.set_linewidth(y.max()*10)

fig, ax = plt.subplots()
line = ax.add_collection(lc)
plt.fill_between(x, y, y2=y.max()+10, interpolate=True, color='white', zorder=2)
plt.plot(x, y, "o-")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("What a nice plot!")

plot_dir = Path("plots")
plot_dir.mkdir(exist_ok=True)
plt.savefig(plot_dir / "my_plot.png")
