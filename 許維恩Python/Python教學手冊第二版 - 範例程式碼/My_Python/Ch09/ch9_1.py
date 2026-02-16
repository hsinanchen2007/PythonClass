# ch9_1.py, permutation()和shuffle()的差異
import numpy as np
rg = np.random.default_rng()   		# 建立亂數生成器

arr = np.array([1, 2, 3, 4]) 			# 初始化一個陣列
permuted_arr = rg.permutation(arr)  	# 使用permutation ()
print('permutation() 產生的新陣列：', permuted_arr)
print('permutation() 後的原始陣列：', arr)  	
 
arr = np.array([1, 2, 3, 4]) 			# 重新初始化陣列
rg.shuffle(arr) 						# 使用 shuffle()
print('shuffle() 打亂後的原始陣列：', arr)