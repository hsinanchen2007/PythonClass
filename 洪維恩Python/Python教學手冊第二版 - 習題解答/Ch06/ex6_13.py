# ex6_13.py
# 定義集合 s1
s1 = {3, 2, 2, 1, 4, 5}
print('s1=',s1)
# (a) 求 s1 元素的個數
num_elements = len(s1)
print("(a) s1 的元素個數:", num_elements)

# (b) 判別元素 0 是否在 s1 裡
is_0_in_s1 = 0 in s1
print("(b) 元素 0 是否在 s1 裡:", is_0_in_s1)

# (c) 判別 {0, 1, 2} 是否小於等於 s1
is_subset = {0, 1, 2} <= s1
print("(c) {0, 1, 2} 是否小於等於 s1:", is_subset)

# (d) 判別 set(range(9)) 是否大於 s1
is_greater = set(range(9)) > s1
print("(d) set(range(9)) 是否大於 s1:", is_greater)

'''output------------------------------
s1= {1, 2, 3, 4, 5}
(a) s1 的元素個數: 5
(b) 元素 0 是否在 s1 裡: False
(c) {0, 1, 2} 是否小於等於 s1: False
(d) set(range(9)) 是否大於 s1: True
------------------------------------'''