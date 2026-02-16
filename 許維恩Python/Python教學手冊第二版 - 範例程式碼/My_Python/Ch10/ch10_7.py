# ch10_7.py, 找出最小距離的兩個點, 廣播版
import numpy as np
pa = np.array([[2, 4, 5],     		# x 座標 (3 個點)
                 [3, 3, 4]])    		# y 座標
pb = np.array([[3, 4, 5, 6],     	# x 座標 (4 個點)
                 [0, 7, 2, 1]])    	# y 座標

# 使用 broadcasting 計算差值, shape: (2, 3, 4)
diff = pa[:, :, None] - pb[:, None, :]

# 將diff平方後加總，得到距離平方陣列, shape: (3, 4)
d2 = np.sum(diff**2, axis=0)

# 找出距離平方最小的位置
ma, mb = np.unravel_index(np.argmin(d2), d2.shape)
print(f'pa: {ma}, pb: {mb}, 距離平方為：{d2[ma, mb]:.2f}')