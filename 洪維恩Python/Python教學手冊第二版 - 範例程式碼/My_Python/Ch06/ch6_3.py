# ch6_3.py, 比較串列與元組的元素位址變化
lst = [10, 20, 30]   	# 串列
tpl = (10, 20, 30)   	# 元組

print('修改前:')    	# 印出元素的 id（記憶體位址）
print('id(lst[0]):', id(lst[0]))  
print('id(tpl[0]):', id(tpl[0]))  

lst[0] = 99  			# 串列允許修改
# tpl[0] = 99  		# 這行會出錯，因為元組不可變

print('修改 lst[0] 後:')
print('id(lst[0]):',id(lst[0]))  # id改變，表示lst[0]指向新物件
print('lst:', lst)