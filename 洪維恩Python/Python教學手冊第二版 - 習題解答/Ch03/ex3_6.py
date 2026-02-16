# ex3_6.py
import random
# (a) 產生一個 0 到 1 之間的亂數
rand_num = random.random()

# (b) 從字串 "Significant" 中隨機抽取3個字元
rand_chars = random.sample("Significant", 3)  # 不重複抽取

# (c) 產生一個 1 到 6 之間的整數亂數
rand_int = random.randint(1, 6)

# (d) 從 1 到 10 之間的偶數隨機挑選一個數
rand_even = random.choice([2, 4, 6, 8, 10])  

# (e) 產生一個介於 -1 到 1 之間的浮點數亂數
rand_float = random.uniform(-1, 1)

# 輸出結果
print(f"(a) 0 到 1 之間的亂數 = {rand_num}")
print(f"(b) 從 'Significant' 中隨機抽取 3 個字元 = {rand_chars}")
print(f"(c) 1 到 6 之間的整數亂數 = {rand_int}")
print(f"(d) 1 到 10 之間的偶數隨機挑選一個數 = {rand_even}")
print(f"(e) 介於 -1 到 1 之間的浮點數亂數 = {rand_float}")

'''output---------------------------------------------------
(a) 0 到 1 之間的亂數 = 0.6258793658882768
(b) 從 'Significant' 中隨機抽取 3 個字元 = ['S', 'f', 't']
(c) 1 到 6 之間的整數亂數 = 2
(d) 1 到 10 之間的偶數隨機挑選一個數 = 10
(e) 介於 -1 到 1 之間的浮點數亂數 = 0.6510928183881299
---------------------------------------------------------'''