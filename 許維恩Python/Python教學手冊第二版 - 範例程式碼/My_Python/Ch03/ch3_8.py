# ch3_8.py, 模擬「購物清單」的操作
lst = []  # 建立購物清單

lst.append('牛奶')			# 使用 append() 增加品項
lst.append('麵包')
print('目前清單:', lst)  

lst.insert(1, '雞蛋')			# 使用 insert() 插入品項
print('插入雞蛋後:', lst)  

lst.extend(['荔枝', '咖啡'])	# 使用 extend() 加入多個品項
print('加入多個品項後:', lst)  

lst.remove('麵包')			# 使用 remove() 移除品項
print('移除麵包後:', lst)  

item = lst.pop()				# 使用 pop() 取出最後一項
print('取出最後一項:', item)  
print('更新後的清單:', lst)  

lst.clear()					# 使用 clear() 清空清單
print('購物完成後:', lst) 