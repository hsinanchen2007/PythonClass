# ex11_14.py
import matplotlib.pyplot as plt

# 定義四季的降雨量
rainfall = [138, 187, 92, 63]
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# 繪製圓餅圖
plt.figure(figsize=(6, 6))
plt.pie(rainfall, labels=seasons, autopct='%1.1f%%', startangle=90)

plt.title('Rainfall Percentage by Season')# 設定圖標題
plt.show()  # 顯示圖形

'''output----------------------

----------------------------'''