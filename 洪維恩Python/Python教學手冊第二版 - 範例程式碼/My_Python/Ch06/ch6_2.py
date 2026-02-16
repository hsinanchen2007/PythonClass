# ch6_2.py, 設定運算、淺拷貝和深拷貝的比較
import copy  				# 載入 copy 模組
lst = [[1, 2], 34]		# 建立一個原始串列

# 設定運算（指向同一個 list）
a = lst   				# a 和 lst 指向相同的記憶體位址
a[0][0] = 99  			# 修改 a[0][0]
print('設定運算:', lst)	# [[99, 2], 34]，lst 也被修改

# 淺拷貝：copy()
lst = [[1, 2], 34]		# 重設 lst
b = lst.copy()			# 建立淺拷貝
b[0][0] = 99 				# 修改 b[0][0]
print('淺拷貝:', lst)		# [[99, 2], 34]，lst 仍然被影響

# 深拷貝：copy.deepcopy()
lst = [[1, 2], 34]  		# 重設 lst
c = copy.deepcopy(lst)	# 建立深拷貝
c[0][0] = 99  # 修改 c[0][0]
print('深拷貝:', lst)  	# [[1, 2], 34]，lst 不受影響  