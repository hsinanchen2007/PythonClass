# ex3_7.py
import random
# 設定亂數種子
random.seed(37)

# (a) 產生一個 1 到 100 之間（包含100）的整數亂數
rand_int = random.randint(1, 100)

# (b) 從字串 'Halloween' 中隨機抽取 4 個字元
rand_chars = random.sample("Halloween", 4)

# (c) 從串列 [12, 38, 54, 64, 77, 29] 中隨機挑選兩個數
my_list1 = [12, 38, 54, 64, 77, 29]
rand_list = random.sample(my_list1, 2)

# (d) 將 my_list 裡的元素打亂
my_list2 = [2, 3, 5, 8, 9]
random.shuffle(my_list2)  # 直接改變 my_list2 本身

# 輸出結果
print(f"(a) 1 到 100 之間的整數亂數 = {rand_int}")
print(f"(b) 從 'Halloween' 中隨機抽取 4 個字元 = {rand_chars}")
print(f"(c) 從串列 [12, 38, 54, 64, 77, 29] 中隨機挑選兩個數 = {rand_list}")
print(f"(d) my_list 打亂後的結果 = {my_list2}")

'''output-------------------------------------------------------
(a) 1 到 100 之間的整數亂數 = 88
(b) 從 'Halloween' 中隨機抽取 4 個字元 = ['a', 'H', 'w', 'l']
(c) 從串列 [12, 38, 54, 64, 77, 29] 中隨機挑選兩個數 = [64, 77]
(d) my_list 打亂後的結果 = [9, 3, 5, 8, 2]
-------------------------------------------------------------'''