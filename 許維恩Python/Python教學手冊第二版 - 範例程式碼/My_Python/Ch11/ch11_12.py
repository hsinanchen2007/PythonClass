# ch11_12.py, 在圖形上加上註解文字和箭號
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 200)
fig, ax = plt.subplots()
ax.plot(x, x*np.sin(x), x, x*np.cos(x))
ax.annotate('x sin(x)', xy=(2.5,2.5), xytext=(2.5,6), fontsize=12,
    arrowprops = dict(arrowstyle='->', facecolor='black'))
ax.annotate('x cos(x)',xy=(8,-5), xytext=(6,-9), fontsize=12,
    arrowprops = dict(arrowstyle='-', facecolor='black'))
ax.text(4, 11,'Annotaion', fontsize=18, color='r')
ax.grid()
plt.show()