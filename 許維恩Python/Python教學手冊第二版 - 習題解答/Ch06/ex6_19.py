# ex6_19.py
# (a) 使用 fromkeys() 建立字典
keys = ['Jan', 'Feb', 'Mar']
d1 = dict.fromkeys(keys, None)
print("(a) 建立的字典 d1:", d1)

# (b) 修改字典 d1 中的值
d1['Jan'] = 1
d1['Feb'] = 2
d1['Mar'] = 3
print("(b) 修改後的 d1:", d1)

# (c) 使用 update() 函數將 {'Apr': 4} 加入 d1
d1.update({'Apr': 4})
print("(c) 使用 update() 加入的 d1:", d1)

# (d) 使用 pop() 刪除鍵為 'Feb' 的鍵值對
removed_value = d1.pop('Feb')
print("(d) 刪除後的 d1:", d1, end=' ')
print(", 被刪除的值:", removed_value)

'''output----------------------------------------------------------------
(a) 建立的字典 d1: {'Jan': None, 'Feb': None, 'Mar': None}
(b) 修改後的 d1: {'Jan': 1, 'Feb': 2, 'Mar': 3}
(c) 使用 update() 加入的 d1: {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4}   
(d) 刪除後的 d1: {'Jan': 1, 'Mar': 3, 'Apr': 4} , 被刪除的值: 2
----------------------------------------------------------------------'''