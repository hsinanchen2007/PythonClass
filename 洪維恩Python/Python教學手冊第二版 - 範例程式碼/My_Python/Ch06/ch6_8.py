# ch6_8.py, 字典的淺拷貝
# 預設贈品清單
default = {
    'user': 'customer',
    'gifts': ['A', 'B']
}

a_copy = default.copy()   		# 顧客a的贈品清單（淺拷貝）
a_copy['user'] = 'Isabelle'  	# 修改顧客a的名字
a_copy['gifts'].append('C')  	# 顧客a新增一個贈品

print('預設清單: ', default)  	# 出現問題：預設清單被修改
print('顧客a清單:', a_copy) 