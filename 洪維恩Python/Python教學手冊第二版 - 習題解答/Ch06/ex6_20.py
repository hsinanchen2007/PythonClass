# ex6_20.py
d1 = {'large': 34, 'medium': 28, 'small': 20}

# (a) 建立由所有鍵組成的串列
keys_list = list(d1.keys())
print("(a) 所有的鍵組成的串列:", keys_list)

# (b) 建立由所有值組成的元組
values_tuple = tuple(d1.values())
print("(b) 所有的值組成的元組:", values_tuple)

# (c) 建立由所有鍵值對組成的串列
items_list = list(d1.items())
print("(c) 所有的鍵值對組成的串列:", items_list)

# (d) 使用 setdefault('large', 36)
result = d1.setdefault('large', 36)
print("(d) 執行 setdefault('large', 36) 後的 d1:", d1, end=' ')
print(", 返回的結果:", result)

# (e) 使用 setdefault('xlarge', 40)
result = d1.setdefault('xlarge', 40)
print("(e) 執行 setdefault('xlarge', 40) 後的 d1:", d1, end=' ')
print(", 返回的結果:", result)

'''output-------------------------------------------------------------------------------------------------------------
(a) 所有的鍵組成的串列: ['large', 'medium', 'small']
(b) 所有的值組成的元組: (34, 28, 20)
(c) 所有的鍵值對組成的串列: [('large', 34), ('medium', 28), ('small', 20)]
(d) 執行 setdefault('large', 36) 後的 d1: {'large': 34, 'medium': 28, 'small': 20} , 返回的結果: 34
(e) 執行 setdefault('xlarge', 40) 後的 d1: {'large': 34, 'medium': 28, 'small': 20, 'xlarge': 40} , 返回的結果: 40
-------------------------------------------------------------------------------------------------------------------'''

'''說明-------------------------------------------------------------------------
(d) 使用 setdefault('large', 36) 不會改變 d1，因為鍵 'large' 已經存在，傳回 34。
(e) 使用 setdefault('xlarge', 40) 會將鍵 'xlarge' 添加到字典中，並傳回 40。
-------------------------------------------------------------------------------'''