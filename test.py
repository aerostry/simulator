from dedalus import public as de
import numpy as np
import matplotlib.pyplot as plt

de.logging_setup.rootlogger.setLevel('ERROR')


xbasis = de.Chebyshev('x', 32, interval=(0,5), dealias=3/2)

grid_normal = xbasis.grid(scale=1)
grid_dealias = xbasis.grid(scale=3/2)

plt.figure(figsize=(10, 1))
plt.plot(grid_normal, np.zeros_like(grid_normal)+1, 'o', markersize=5)
plt.plot(grid_dealias, np.zeros_like(grid_dealias)-1, 'o', markersize=5)
plt.ylim([-2, 2])
plt.gca().yaxis.set_ticks([]);

xb1 = de.Chebyshev('x1', 16, interval=(0,2))
xb2 = de.Chebyshev('x2', 32, interval=(2,8))
xb3 = de.Chebyshev('x3', 16, interval=(8,10))
xbasis = de.Compound('x', (xb1, xb2, xb3))

compound_grid = xbasis.grid(scale=1)

plt.figure(figsize=(10, 1))
plt.plot(compound_grid, np.zeros_like(compound_grid), 'o', markersize=5)
plt.gca().yaxis.set_ticks([]);
