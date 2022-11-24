import matplotlib.pyplot as plt
import numpy as np

points = []
time = []

for t in np.arange(0.0, 2.0, 0.01):
       point = sine = 1 + np.sin(2 * np.pi * t)
       points.append(point)
       time.append(t)

fig, ax = plt.subplots()
ax.plot(time, points)

ax.set(xlabel='time [s]', ylabel='value [-]',
       title='vybrana funkce')
ax.grid(visible=None, which="major", axis="y")

plt.show()