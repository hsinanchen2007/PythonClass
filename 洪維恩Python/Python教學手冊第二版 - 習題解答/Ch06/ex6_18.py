# ex6_18.py
d1 = {0: 'red', 1: 'green', 2: 'blue'}
print('d1=',d1)
# (a) 查詢鍵為 1 的值
value = d1[1]
print("(a) 鍵為 1 的值:", value)

# (b) 將鍵為 2 的值修改為 'yellow'
d1[2] = 'yellow'
print("(b) 修改後的 d1:", d1)

# (c) 刪除鍵為 0 的鍵值對
del d1[0]
print("(c) 刪除鍵為 0 的鍵值對後的 d1:", d1)

# (d) 查詢鍵 4 是否在 d1 中
is_key_present = 4 in d1
print("(d) 鍵 4 是否在 d1 中:", is_key_present)

'''output---------------------------------------------------
d1= {0: 'red', 1: 'green', 2: 'blue'}
(a) 鍵為 1 的值: green
(b) 修改後的 d1: {0: 'red', 1: 'green', 2: 'yellow'}
(c) 刪除鍵為 0 的鍵值對後的 d1: {1: 'green', 2: 'yellow'}
(d) 鍵 4 是否在 d1 中: False
---------------------------------------------------------'''