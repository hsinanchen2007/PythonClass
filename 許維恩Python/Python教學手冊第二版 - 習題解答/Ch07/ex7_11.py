# ex7_11.py
class NumberUtils:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False  # 小於等於 1 的數不是質數
        for i in range(2, int(n**0.5) + 1):  # 只檢查到平方根
            if n % i == 0:  # 如果能被整除，則不是質數
                return False
        return True  # 若無法被整除，則是質數

# 測試
print(NumberUtils.is_prime(11))  # 輸出: True
print(NumberUtils.is_prime(15))  # 輸出: False

'''output------
True
False
------------'''