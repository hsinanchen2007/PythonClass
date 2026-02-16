# ex8_18_m2.py
from ex8_18_m1 import digits  # 匯入 digits 函數
def is_armstrong(n):
    d = digits(n)
    power = len(d)  # 幾位數
    total = sum([x ** power for x in d])  # 每位數的 n 次方加總
    return total == n
