# ch11_26.py, 直方圖繪製
import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(0, 1, 4096)

fig, ax = plt.subplots(1, 2, figsize = (12, 4))
ax[0].hist(x, bins=20, edgecolor='black', alpha=0.5) # 繪製直方圖
ax[0].set_title('Normal distribution')

ax[1].hist(x, rwidth=0.8, cumulative=True, bins=20, alpha=0.5)
ax[1].set_title('Cumulative distribution')
plt.show()