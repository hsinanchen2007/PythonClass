# ex6_4.py
lst = [9, 8, 7, 1, 2, 3, 7, 3, 2]   # 原始串列
# (a) 取出索引 0 到 2 的元素（含索引 2）
result_a = lst[0:3]
print("(a)", result_a)

# (b) 取出最後 3 個元素
result_b = lst[-3:]
print("(b)", result_b)

# (c) 取出索引 4 到 7 的元素（含索引 4）
result_c = lst[4:8]
print("(c)", result_c)

# (d) 取出索引為偶數的元素（不包含索引 0）
result_d = lst[2::2]
print("(d)", result_d)

# (e) 找出長度、最大值、最小值，並計算總和
length = len(lst)
max_value = max(lst)
min_value = min(lst)
total_sum = sum(lst)
print("(e) 長度:",length,", 最大值:",max_value,", 最小值:",min_value,", 總和:",total_sum)

# (f) 反向提取倒數第 1 個到倒數第 4 個元素
result_f = lst[-1:-5:-1]
print("(f)", result_f)

# (g) 反向排列
result_g = lst[::-1]
print("(g)", result_g)

'''output---------------------------------------------
(a) [9, 8, 7]
(b) [7, 3, 2]
(c) [2, 3, 7, 3]
(d) [7, 2, 7, 2]
(e) 長度: 9 , 最大值: 9 , 最小值: 1 , 總和: 42
(f) [2, 3, 7, 3]
(g) [2, 3, 7, 3, 2, 1, 7, 8, 9]
---------------------------------------------------'''