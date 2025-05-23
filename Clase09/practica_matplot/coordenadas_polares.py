import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = plt.subplot(111, polar=True) 
# Datos
N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

# Gráfico de barras polares
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Colores y transparencia
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

plt.show()