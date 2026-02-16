# ex12_14.py
import pandas as pd
import matplotlib.pyplot as plt

# 創建 Series 物件 s
s = pd.Series([28, 88, 12, 76, 89], index=list('abcde'))

# 繪製長條圖
ax = s.plot.bar(figsize=(6, 6))

# 設定標題
plt.title('Bar chart')

# 顯示圖形
plt.show()

'''output----------------------

----------------------------'''