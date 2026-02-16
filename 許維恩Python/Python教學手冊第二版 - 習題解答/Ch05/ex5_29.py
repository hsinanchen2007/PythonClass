# ex5_29.py
a = ['P', 'y', 't', 'h', 'o', 'n']
b = [1, 2, 3, 4, 5, 6]

# 手動建立字典
result_dict = {}
for key, value in zip(a, b):
    result_dict[key] = value

print(result_dict)

'''output------------------------------------------
{'P': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n': 6}
------------------------------------------------'''