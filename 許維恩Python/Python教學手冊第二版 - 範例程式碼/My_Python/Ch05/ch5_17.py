# ch5_17.py, lambda表達式
# 不帶參數的 lambda
say_hello = lambda: 'Hello!'
print(say_hello())		# 輸出：Hello!

# 單個參數的 lambda
odd_or_even = lambda x: '奇數' if x % 2 else '偶數'
print(odd_or_even(5))		# 輸出：奇數

# 兩個參數的 lambda
add = lambda x, y: x + y
print(add(3, 7))			# 輸出：10