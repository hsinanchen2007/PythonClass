# ch9_5.py, ravel() 和 flatten() 的區別
import numpy as np
a = np.array([[1, 2], [3, 4]])  		# 原始二維陣列
b = a.ravel()  						# ravel() 傳回view
print('使用 ravel() 後的陣列 b：', b)
b[0] = 100  							# 修改 b[0]
print('修改 b 後的原始陣列 a：\n', a)
print('是否共享記憶體？', np.shares_memory(a, b))  	# True
  
a = np.array([[1, 2], [3, 4]])  		# 重新初始化a 
c = a.flatten()   					# flatten() 傳回copy
print('使用 flatten() 後的陣列 c：', c)
c[0] = 200  							# 修改 c[0]
print('修改 c 後的原始陣列 a：\n', a)
print('是否共享記憶體？', np.shares_memory(a, c))  	# False