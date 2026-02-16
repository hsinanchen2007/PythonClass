# ex5_27.py
# Lambda 函數將負數變 0
replace_negatives = lambda lst: [i if i >= 0 else 0 for i in lst]

# 測試範例
lst = [-3, 6, -4, 6, 8]
print(replace_negatives(lst))

'''output--------------------
[0, 6, 0, 6, 8]
--------------------------'''