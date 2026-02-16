# ex6_8.py
# 定義元組 tpl
tpl = (12, [23, 34], (37, 0, 'cat'))

# (a) 提取 12
result_a = tpl[0]
print("(a)", result_a)

# (b) 提取 [23, 34]
result_b = tpl[1]
print("(b)", result_b)

# (c) 提取 (12, [23, 34])
result_c = tpl[:2]
print("(c)", result_c)

# (d) 提取 'cat'
result_d = tpl[2][2]
print("(d)", result_d)

# (e) 提取 (0, 'cat')
result_e = tpl[2][1:]
print("(e)", result_e)

# (f) 提取 (37, 0, 'cat')
result_f = tpl[2]
print("(f)", result_f)

# (g) 提取 0
result_g = tpl[2][1]
print("(g)", result_g)

# (h) 提取 34
result_h = tpl[1][1]
print("(h)", result_h)

'''output--------------------
(a) 12
(b) [23, 34]
(c) (12, [23, 34])
(d) cat
(e) (0, 'cat')
(f) (37, 0, 'cat')
(g) 0
(h) 34
--------------------------'''