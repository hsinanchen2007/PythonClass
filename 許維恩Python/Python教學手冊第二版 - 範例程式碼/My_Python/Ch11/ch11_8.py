# ch11_8.py, 同時畫兩張圖，並加入圖例(legend)
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 48)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label='sin(x)')     # 圖例的標籤為 sin(x)
ax.plot(x, np.cos(x), label='cos(x)', linewidth=5)
ax.legend(loc = 'lower left')    # 加入圖例，並置於圖形的左下方
plt.show()