# ex10_17.py
import numpy as np
# 隨機生成顏色陣列 c，形狀為 (3, 10)
np.random.seed(0)  # 設定隨機種子以便重現結果
c = np.random.randint(0, 256, (3, 10))

# 顏色 a
a = np.array([37, 65, 182])
print("顏色：", a)
# 利用 NumPy 廣播來找出最相近的顏色
diffs = np.linalg.norm(c - a[:, np.newaxis], axis=0)  # 計算所有顏色與 a 的歐氏距離
closest_color_no_for = c[:, np.argmin(diffs)]  # 找出距離最短的顏色

print("最相近顏色：", closest_color_no_for)

'''output----------------------------------
顏色： [ 37  65 182]
最相近顏色： [67 70 88]
----------------------------------------'''