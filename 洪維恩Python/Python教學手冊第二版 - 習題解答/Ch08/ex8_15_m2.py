# ex8_15_m2.py
from ex8_15_m1 import factors  # 匯入自訂模組中的函數
def is_prime(p):
    return len(factors(p)) == 2  # 只有 1 和自己本身才是質數