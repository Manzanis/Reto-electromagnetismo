import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

size = 9
min = -2
max = 2

x = np.linspace(min, max, size)
y = np.linspace(min, max, size)
X,Y = np.meshgrid(x, y)

K = 9e9
q = 20e-6

r2 = x**2 + y**2
angles = np.arctan(r2, x)
Ex = ((K*q)/r2)*np.cos(angles)
Ey = ((K*q)/r2)*np.sin(angles)

fig, ax = plt.subplots(figsize = (7,7))

ax.quiver(X, Y, Ex, Ey)
ax.scatter(0, 0, c='red', s=1000)
ax.axis([-2,2,-2,2])
ax.set_aspect('equal', 'box')

mags = 10
