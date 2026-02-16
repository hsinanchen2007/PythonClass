# ex7_3.py
import math
class Calculator:
    def __init__(self, a, b):
        self.n1 = a
        self.n2 = b

    def add(self):
        return self.n1 + self.n2

    def gcd(self):
        return math.gcd(self.n1, self.n2)

    def lcm(self):
        return abs(self.n1 * self.n2) // math.gcd(self.n1, self.n2)

    def power(self):
        return self.n1 ** self.n2

# 測試
c0 = Calculator(2, 10)
print(c0.add())    # 輸出: 12
print(c0.gcd())    # 輸出: 2
print(c0.lcm())    # 輸出: 10
print(c0.power())  # 輸出: 1024

'''output------
12
2
10
1024
------------'''