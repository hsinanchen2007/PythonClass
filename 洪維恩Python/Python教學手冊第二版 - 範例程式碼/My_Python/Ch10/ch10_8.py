# ch10_8.py, 迴圈和廣播所需時間的比較
import numpy as np
from time import time					# 載入time函數
def dist_for(pa, pb):  				#  for 迴圈版本
    d2 = np.zeros((pa.shape[1], pb.shape[1]))
    for i in range(pa.shape[1]):      	# a 中的點
        for j in range(pb.shape[1]):  	# b 中的點
            d2[i,j] = np.sum((pa[:, i] - pb[:, j])**2)

def dist_broadcast(pa, pb):   			# 廣播版本
    diff = pa[:, :, np.newaxis] - pb[:, np.newaxis, :]
    d2 = np.sum(diff**2, axis=0)

np.random.seed(0)
pa = np.random.randint(0, 100, size=(2, 1000))  # 1000 個點
pb = np.random.randint(0, 100, size=(2, 1200))  # 1200 個點
 
start = time()      		# 測試 for 迴圈版本
dist_for(pa, pb)  
print(f'[迴圈版本] 花費時間：{time() - start:.4f} 秒')
 
start = time()      		# 測量 broadcasting 版本
dist_broadcast(pa, pb)
print(f'[廣播版本] 花費時間：{time() - start:.4f} 秒')