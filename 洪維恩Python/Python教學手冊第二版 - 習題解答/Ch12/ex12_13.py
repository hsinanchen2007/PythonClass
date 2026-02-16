# ex12_13.py
import pandas as pd
import matplotlib.pyplot as plt

# 創建 Series 物件 s
s = pd.Series([28, 88, 12, 76, 89], index=list('abcde'))

# 繪製圓餅圖並標註百分比
ax = s.plot.pie(autopct='%1.1f%%', figsize=(6, 6))

# 顯示圖形
plt.title("PIE chart")
plt.show()

'''output----------

----------------'''