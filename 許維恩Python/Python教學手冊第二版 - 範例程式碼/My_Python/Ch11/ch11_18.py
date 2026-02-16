# ch11_18.py, 設定座標軸的顯示位置
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1.7, 6, 32)
y = x**3 - 6*x**2 + 3*x + 2

fig, ax = plt.subplots(1, 2, figsize = (12, 4))
ax[0].plot(x,y)
ax[0].spines['right'].set_visible(False)    # 設右邊軸線不可見 
ax[0].spines['top'].set_visible(False)      # 設上面軸線不可見 

ax[1].plot(x,y,'r:')
ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)
ax[1].spines['bottom'].set_position(('data', 0)) # 下面軸線的位置
ax[1].spines['left'].set_position(('data', 0))  	 # 左邊軸線的位置
plt.show()