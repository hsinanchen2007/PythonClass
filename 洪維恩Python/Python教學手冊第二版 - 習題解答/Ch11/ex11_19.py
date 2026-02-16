# ex11_19.py
import numpy as np
import matplotlib.pyplot as plt

# 生成亂數
x = np.random.uniform(0, 6, 1000)  # x 的亂數，範圍 [0, 6]
y = np.random.uniform(0, 6, 1000)  # y 的亂數，範圍 [0, 6]
z = np.random.normal(5, 8, 1000)  # z 的常態分佈亂數，平均值5，標準差8

# 繪製散佈圖，顏色根據 z 值來設
plt.scatter(x, y, c=z, cmap='jet', alpha=0.7)

# 添加顏色條
plt.colorbar(label='z values')

# 設定標題和標籤
plt.title('Scatter Plot of Random Values')
plt.xlabel('x values')
plt.ylabel('y values')

plt.show()  # 顯示圖形

'''output---------------------------------------

---------------------------------------------'''