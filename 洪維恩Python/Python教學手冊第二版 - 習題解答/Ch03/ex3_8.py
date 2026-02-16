# ex3_8.py
import random
# 設定亂數種子
random.seed(199)

# (a) 隨機從字串 'abcdefg' 中選擇一個字元
rand_char = random.choice("abcdefg")

# (b) 從串列 [12, 34, 56, 78, 90] 中隨機選擇 3 個元素（不重複）
rand_sample = random.sample([12, 34, 56, 78, 90], 3)

# (c) 隨機打亂串列 [1, 2, 3, 4, 5] 的元素順序
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

# (d) 產生一個 0 到 1 之間的浮點數（不包含 1）
rand_float = random.random()

# (e) 從字串 'abcd' 中選擇 5 個字元，允許重複選擇
rand_choices = random.choices("abcd", k=5)

# 輸出結果
print(f"(a) 隨機選擇一個字元 = {rand_char}")
print(f"(b) 隨機選擇 3 個元素（不重複）= {rand_sample}")
print(f"(c) 隨機打亂後的串列 = {my_list}")
print(f"(d) 產生的浮點數 = {rand_float}")
print(f"(e) 隨機選擇 5 個字元（允許重複）= {rand_choices}")

'''output-------------------------------------------------------
(a) 隨機選擇一個字元 = c
(b) 隨機選擇 3 個元素（不重複）= [78, 56, 90]
(c) 隨機打亂後的串列 = [4, 5, 2, 1, 3]
(d) 產生的浮點數 = 0.25521588503348214
(e) 隨機選擇 5 個字元（允許重複）= ['d', 'b', 'c', 'a', 'c']
-------------------------------------------------------------'''