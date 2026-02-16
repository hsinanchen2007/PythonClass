# ex5_26.py
# Lambda 函數篩選 0 到 255 之間的數
filter_range = lambda lst: [i for i in lst if 0 <= i <= 255]

# 測試範例
lst = [-3, 6, 100, 300]
print(filter_range(lst))

'''output--------------------
[6, 100]
--------------------------'''