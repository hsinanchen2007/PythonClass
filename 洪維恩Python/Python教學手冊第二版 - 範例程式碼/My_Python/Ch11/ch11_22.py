# ch11_22.py, 散佈圖
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 30)
y = x + np.random.rand(len(x))
fig, ax = plt.subplots(1, 2, figsize = (12, 4))
ax[0].scatter(x, y)   # 散佈圖
ax[1].scatter(x, y, marker='^', color='red') # 修改標記符號和顏色
plt.show()