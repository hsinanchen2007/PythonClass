# ch11_19.py, 將兩條曲線之間的區域填滿
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 200)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), 'r')
ax.plot(x, np.cos(2*x), 'b')
ax.fill_between(x, np.cos(2*x), np.sin(x), alpha=0.5, color='yellow')
plt.show()