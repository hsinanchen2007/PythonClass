# ex6_9.py
# 定義元組 tpl
tpl = (12, 65, 37, 37, 34, 65, 37)

# (a) 求 tpl 的最大值、最小值與總和
max_value = max(tpl)
min_value = min(tpl)
total_sum = sum(tpl)
print("(a) 最大值:", max_value, "最小值:", min_value, "總和:", total_sum)

# (b) 判別 66 是否在 tpl 裡
is_66_in_tpl = 66 in tpl
print("(b) 66 是否在 tpl 裡:", is_66_in_tpl)

# (c) 找出元素 34 在 tpl 裡的索引
index_34 = tpl.index(34)
print("(c) 元素 34 在 tpl 裡的索引:", index_34)

# (d) 統計元素 37 在 tpl 裡出現的個數
count_37 = tpl.count(37)
print("(d) 元素 37 在 tpl 裡出現的個數:", count_37)

'''output----------------------------------
(a) 最大值: 65 最小值: 12 總和: 287
(b) 66 是否在 tpl 裡: False
(c) 元素 34 在 tpl 裡的索引: 4
(d) 元素 37 在 tpl 裡出現的個數: 3
----------------------------------------'''