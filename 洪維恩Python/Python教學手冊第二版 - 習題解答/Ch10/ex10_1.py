# ex10_1.py
import math
# 設定變數
a = -2.3
b = 5.75
print('a=', a, 'b=',b)

# (a) 絕對值
abs_a = abs(a)

# (b) 比 a 大的最小整數（天花板函數）
ceil_a = math.ceil(a)

# (c) 比 b 小的最大整數（地板函數）
floor_b = math.floor(b)

# (d) 四捨五入到小數第1位
round_b = round(b, 1)

# (e) 以2為底的對數
log2_b = math.log2(b)

# (f) b 的平方根
sqrt_b = math.sqrt(b)

# 輸出結果
print(f"(a) 絕對值：{abs_a}")
print(f"(b) 比 a 大的最小整數：{ceil_a}")
print(f"(c) 比 b 小的最大整數：{floor_b}")
print(f"(d) 捨入到小數第1位：{round_b}")
print(f"(e) 以 2 為底的對數：{log2_b}")
print(f"(f) 平方根：{sqrt_b:.3f}")

'''output------------------------------------
a= -2.3 b= 5.7
(a) 絕對值：2.3
(b) 比 a 大的最小整數：-2
(c) 比 b 小的最大整數：5
(d) 捨入到小數第1位：5.8
(e) 以 2 為底的對數：2.523561956057013
(f) 平方根：2.398
------------------------------------------'''