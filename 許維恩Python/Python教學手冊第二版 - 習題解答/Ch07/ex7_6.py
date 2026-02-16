# ex7_6.py
class Circle:
    pi = 3.14159  # 類別屬性 pi，初始值為 3.14159

    def __init__(self, radius):
        self.radius = radius  # 實例屬性 radius，圓的半徑

    def area(self):
        return Circle.pi * (self.radius ** 2)  # 使用類別屬性 pi 計算面積

    def perimeter(self):
        return 2 * Circle.pi * self.radius  # 使用類別屬性 pi 計算周長

# 測試
c1 = Circle(5)
print(f'面積: {c1.area():.2f}')          # 輸出: 面積: 78.54
print(f'周長: {c1.perimeter():.2f}')     # 輸出: 周長: 31.42

Circle.pi = 3.14  # 修改類別屬性 pi 的值
c2 = Circle(5)
print(f'面積: {c2.area():.2f}')          # 輸出: 面積: 78.50
print(f'周長: {c2.perimeter():.2f}')     # 輸出: 周長: 31.40

'''output----------
面積: 78.54
周長: 31.42
面積: 78.50
周長: 31.40
----------------'''