# ch10_4.py, where() 與索引轉換函數應用
import numpy as np
scores = np.array([		# 甜甜圈得分資料（3 家店，4 種口味）
    [ 87, 100,  92, 75],	# 第0號店
    [100,  85, 100, 60], 	# 第1號店
    [ 88,  90,  87, 73] 	# 第2號店
])
max_pos = np.where(scores == 100)  		# 找出所有滿分的 index

# 轉換成一維索引（方便儲存, 轉換後的值應為 [1, 4, 6]）
indices = np.ravel_multi_index(max_pos, scores.shape)

# 從一維還原回 (店號, 口味)
unraveled = np.unravel_index(indices, scores.shape)
for store, flavor in zip(*unraveled):
    print(f'第 {store} 號店，第 {flavor} 種口味')