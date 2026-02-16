# ch2_1.py, 運算子使用範例
a = 2 ** 3		# 次方運算，2 的 3 次方
b = 20 % 7		# 取餘數，20 除以 7 的餘數

# 比較運算子
is_equal = (a == b)	# 判斷是否相等
is_greater = (a > b)	# 判斷是否大於

# 邏輯運算子
result = is_equal or is_greater		# 邏輯 or 運算

# 輸出結果
print('a:', a, 'b:', b)
print('比較結果:', is_equal, is_greater)
print('邏輯結果:', result)