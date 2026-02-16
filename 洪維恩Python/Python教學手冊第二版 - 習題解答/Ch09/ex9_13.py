# ex9_13.py
import numpy as np
a = np.array([0, 1, 2, 3, 4, 5])
print('a=',a)
# (a) b = a[3:] → 切片，會是 view（檢視）
b = a[3:]
b[0] = 99
print("(a)", a)  # a[3] 會變成 99

# (b) b = a[::-1] → 反向切片，仍是 view
a = np.array([0, 1, 2, 3, 4, 5])
b = a[::-1]
b[0] = 88
print("(b)", a)  # a[5] 會變成 88

# (c) b = a.reshape(2,3) → 只是改形狀，不改資料，是 view
a = np.array([0, 1, 2, 3, 4, 5])
b = a.reshape(2, 3)
b[0, 0] = 77
print("(c)", a)  # a[0] 會變成 77

# (d) b = np.random.permutation(a) → 產生新陣列，是 copy（複製）
a = np.array([0, 1, 2, 3, 4, 5])
b = np.random.permutation(a)
b[0] = 66
print("(d)", a)  # a 不會被改到

# (e) b = a[[0,3,4]] → 花式索引，會產生 copy
a = np.array([0, 1, 2, 3, 4, 5])
b = a[[0, 3, 4]]
b[0] = 55
print("(e)", a)  # a 不會被改到

# (f) b = a[1:4] → 切片，是 view
a = np.array([0, 1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 44
print("(f)", a)  # a[1] 會變成 44

# (g) b = a → b 和 a 是同一個東西，共用記憶體
a = np.array([0, 1, 2, 3, 4, 5])
b = a
b[0] = 33
print("(g)", a)  # a[0] 會變成 33

# (h) b = a.copy() → 明確複製，是 copy
a = np.array([0, 1, 2, 3, 4, 5])
b = a.copy()
b[0] = 22
print("(h)", a)  # a 不變

# (i) b = np.random.choice(a, 4) → 隨機抽樣，是 copy
a = np.array([0, 1, 2, 3, 4, 5])
b = np.random.choice(a, 4)
b[0] = 11
print("(i)", a)  # a 不變

# (j) b = a[a > 3] → 布林條件篩選，會產生 copy
a = np.array([0, 1, 2, 3, 4, 5])
b = a[a > 3]
b[0] = 99
print("(j)", a)  # a 不變

'''output-------------------
a= [0 1 2 3 4 5]
(a) [ 0  1  2 99  4  5]
(b) [ 0  1  2  3  4 88]
(c) [77  1  2  3  4  5]
(d) [0 1 2 3 4 5]
(e) [0 1 2 3 4 5]
(f) [ 0 44  2  3  4  5]
(g) [33  1  2  3  4  5]
(h) [0 1 2 3 4 5]
(i) [0 1 2 3 4 5]
(j) [0 1 2 3 4 5]
-------------------------'''

'''output-------------------------------------------------------------------------
(a)	b = a[3:]	                    View	是「切片」，共用記憶體，改 b 會影響 a
(b)	b = a[::-1]	                    View	雖然反向切片，但仍然是檢視
(c)	b = a.reshape(2,3)	            View	改形狀不會複製資料，仍共用記憶體
(d)	b = np.random.permutation(a)	Copy	打亂順序會產生一個新的陣列
(e)	b = a[[0,3,4]]	                Copy	花式索引會回傳新的陣列，不共用記憶體
(f)	b = a[1:4]	                    View	是「切片」，所以是檢視
(g)	b = a	                        View	b 就是 a，是同一個東西
(h)	b = a.copy()	                Copy	明確要求複製，是新的資料
(i)	b = np.random.choice(a, 4)	    Copy	抽樣會產生新陣列
(j)	b = a[a > 3]	                Copy	布林篩選會建立一個新的陣列
-------------------------------------------------------------------------------'''