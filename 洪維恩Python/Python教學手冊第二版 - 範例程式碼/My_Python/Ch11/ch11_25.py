# ch11_25.py, 圓餅圖
import matplotlib.pyplot as plt
labels = ['pony', 'kitten', 'puppy', 'piggy']
sizes = [15, 30, 45, 10]
colors = ['yellow', 'gold', 'lightblue', 'pink']
explode = [0, 0.1, 0, 0]  # 設定分離的比例

fig,ax=plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_aspect('equal')
plt.show()