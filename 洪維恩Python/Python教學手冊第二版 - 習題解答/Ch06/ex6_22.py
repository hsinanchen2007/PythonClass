# ex6_22.py
def invert_dict(d):
    inverted = {}  # 用來存放反轉後的字典
    for key, value in d.items():
        inverted[value] = key  # 將值作為新的鍵，鍵作為新的值
    return inverted

# 測試範例
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dict(original_dict)
print(inverted_dict)  # 輸出應為 {1: 'a', 2: 'b', 3: 'c'}

'''output--------------------
{1: 'a', 2: 'b', 3: 'c'}
--------------------------'''