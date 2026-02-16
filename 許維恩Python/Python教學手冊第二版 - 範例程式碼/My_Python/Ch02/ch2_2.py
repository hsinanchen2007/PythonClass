# ch2_2.py, 複合設值和運算子優先順序範例
a = 10
b = 5

# 複合設值運算
a += 3      				# 相當於 a = a + 3
b *= 2      				# 相當於 b = b * 2
print('a:', a, 'b:', b)

# 運算子優先順序
result = a + b * 2   		# 先乘法後加法，相當於 a + (b * 2)
print('result:', result)

# 括號改變優先順序
result2 = (a + b) * 2  	# 先加法後乘法
print('result2:', result2)