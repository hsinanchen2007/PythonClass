# ch6_9.py, 字典的深拷貝
import copy
default = {     # 預設贈品清單
    'user': 'customer',
    'gifts': ['A', 'B']
}

a_copy = copy.deepcopy(default)	# 顧客a的贈品清單（深拷貝）
a_copy['user'] = 'Isabelle'  		# 修改顧客a的名字
a_copy['gifts'].append('C')  		# 顧客a新增一個贈品

print('預設清單: ', default)  		# 這行不會出現問題了
print('顧客a清單:', a_copy)