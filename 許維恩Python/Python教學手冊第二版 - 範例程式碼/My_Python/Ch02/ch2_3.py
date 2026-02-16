# ch2_3.py, 隱式轉換與顯式轉換      
# 隱式轉換
a = 5      		# 整數
b = 2.5    		# 浮點數
result = a + b  	# 隱式轉換：整數 a 轉為浮點數
print('隱式轉換結果:', result, ', 型別:', type(result))
# 顯式轉換
c = '10'   		# 字串
d = int(c) 		# 顯式轉換：將字串轉為整數
print('顯式轉換結果:', d, ', 型別:', type(d))
print('轉換後 c 的型別:', type(c))    	# c型別不會被改變