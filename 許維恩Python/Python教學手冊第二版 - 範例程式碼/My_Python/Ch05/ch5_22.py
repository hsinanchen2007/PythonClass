# ch5_22.py, 產生器的範例
def gen_test():
    a = 5
    yield a			# 傳回 a 的值
    b = a + 2
    yield b			# 傳回b 的值
    yield b ** 2		# 傳回b 的平方值

gi = gen_test()   	# 呼叫產生成器，得到迭代器物件 gi
# 使用 next() 函數從產生成中依次取值
print(next(gi))		# 輸出: 5
print(next(gi))		# 輸出: 7
print(next(gi))		# 輸出: 49
# print(next(gi))		# 如果再取值一次，會引發 StopIteration 錯誤