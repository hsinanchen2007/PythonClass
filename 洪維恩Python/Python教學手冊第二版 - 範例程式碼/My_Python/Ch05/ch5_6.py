# ch5_6.py, 物件的位址
a = [1, 2, 3]			# 建立串列 [1,2,3], 並讓 a 指向它
b = a   				# b 也指向同一個物件
c = [1, 2, 3]  		# 建立物件c
print('a 指向的物件位址:', id(a))
print('b 指向的物件位址:', id(b))
print('c 指向的物件位址:', id(c))
print('a 和 b 是否指向同一物件？', a is b)    # 回應True

b.append(4) 			# 修改 b 的內容
print('\n修改 b 之後，a 和 b 的值：')
print('a =', a)     	# [1, 2, 3, 4]
print('b =', b)     	# [1, 2, 3, 4]
print('a 指向的物件位址:', id(a))
print('b 指向的物件位址:', id(b))