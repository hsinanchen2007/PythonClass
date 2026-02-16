# ch10_6.py, 找出最小距離的兩個點, for 迴圈版
import numpy as np
pa = np.array([[2, 4, 5],			# pa 的x 座標
                 [3, 3, 4]])			# pa 的y 座標
pb = np.array([[3, 4, 5, 6],		# pb 的x 座標
                 [0, 7, 2, 1]])		# pb 的y 座標
d2 = np.zeros((pa.shape[1], pb.shape[1]))
 
for i in range(pa.shape[1]):      	# pa 中的點
    for j in range(pb.shape[1]):  	# pb 中的點
        d2[i,j] = np.sum((pa[:, i] - pb[:, j])**2)
 
print(d2)
ma, mb = np.unravel_index(np.argmin(d2), d2.shape)
print(f'pa: {ma}, pb: {mb}, 距離平方為：{d2[ma, mb]:.2f}')