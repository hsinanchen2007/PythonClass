# ex11_15.py
import numpy as np
import matplotlib.pyplot as plt

# 產生3600個平均值為1，標準差為5的常態分佈亂數
mean = 1
std_dev = 5
size = 3600
data = np.random.normal(mean, std_dev, size)

# 設定組界數
num_bins = 20

# 計算直方圖的組界
count, bins, patches = plt.hist(data, bins=num_bins, edgecolor='black', alpha=0.7)

# 根據組界的寬度設定長條的寬度
bin_width = bins[1] - bins[0]  # 計算組界寬度
new_width = bin_width * 0.8  # 計算新的長條寬度

# 調整每個長條的寬度
for patch in patches:
    patch.set_width(new_width)

# 設定標題和標籤
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()  # 顯示圖形

'''output----------------------------

----------------------------------'''