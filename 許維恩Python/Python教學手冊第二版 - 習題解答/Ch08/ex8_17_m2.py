# ex8_17_m2.py
from ex8_17_m1 import sum_of_digits  # 匯入 sum_of_digits 函數

def is_harshad(n):
    digit_sum = sum_of_digits(n)
    return n % digit_sum == 0  # 如果 n 能被其數字總和整除，則為 Harshad 數
