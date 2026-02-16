# ch6_4.py, 修改元組中的可變物件
tpl = (4, 'cat', [1, 2])  			# 建立元組

print('修改前:')
print('id(tpl[0]):', id(tpl[0]))	# 整數
print('id(tpl[1]):', id(tpl[1]))	# 字串
print('id(tpl[2]):', id(tpl[2]))	# list

tpl[2].append(3)		# 在 list 裡面新增元素

print('修改後:')
print('id(tpl[2]):', id(tpl[2]))  # list 的位址沒變，但內容變了
print('tpl:', tpl)  	# 印出修改後的 tpl