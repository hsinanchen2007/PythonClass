# ex6_7.py
# 定義 lst
lst = [[17, 21], [98, 12], [33, [44, [21, 38, 35]]], [35, 42]]

# (a) 提取 [17, 21]
result_a = lst[0]
print("(a)", result_a)

# (b) 提取 21
result_b = lst[0][1]
print("(b)", result_b)

# (c) 提取 33
result_c = lst[2][0]
print("(c)", result_c)

# (d) 提取 [35, 42]
result_d = lst[3]
print("(d)", result_d)

# (e) 提取 98
result_e = lst[1][0]
print("(e)", result_e)

# (f) 提取 44
result_f = lst[2][1][0]
print("(f)", result_f)

# (g) 提取 [21, 38, 35]
result_g = lst[2][1][1]
print("(g)", result_g)

# (h) 提取 [38, 35]
result_h = lst[2][1][1][1:]
print("(h)", result_h)

# (i) 提取 [21, 38]
result_i = lst[2][1][1][:2]
print("(i)", result_i)

# (j) 提取 38
result_j = lst[2][1][1][1]
print("(j)", result_j)

# (k) 提取 [[17, 21], [98, 12]]
result_k = lst[:2]
print("(k)", result_k)

# (l) 提取 [44, [21, 38, 35]]
result_l = lst[2][1]
print("(l)", result_l)

'''output--------------------
(a) [17, 21]
(b) 21
(c) 33
(d) [35, 42]
(e) 98
(f) 44
(g) [21, 38, 35]
(h) [38, 35]
(i) [21, 38]
(j) 38
(k) [[17, 21], [98, 12]]
(l) [44, [21, 38, 35]]
--------------------------'''