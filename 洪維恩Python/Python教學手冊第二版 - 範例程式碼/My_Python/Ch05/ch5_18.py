# ch5_18.py, 將lambda表達式傳送到函數裡
def filter_v(func, values):   # 可接收lambda表達式作為參數
    return [v for v in values if func(v)]

# 有名稱的 lambda：篩選偶數
is_even = lambda x: x % 2 == 0
result1 = filter_v(is_even, [3, 4, 6, 7])
print(result1)  # 輸出：[4, 6]

# 匿名的 lambda：篩選大於 5 的數
result2 = filter_v(lambda x: x > 5, [3, 4, 6, 7])
print(result2)  # 輸出：[6, 7] 