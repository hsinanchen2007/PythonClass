# ex7_10.py
class Circle:
    @staticmethod
    def area(radius):
        return 3.14 * radius ** 2  # 計算面積

    @staticmethod
    def perimeter(radius):
        return 2 * 3.14 * radius  # 計算周長

# 測試
radius = 5
print(f'{Circle.area(radius):.2f}')       # 輸出: 78.50
print(f'{Circle.perimeter(radius):.2f}')  # 輸出: 31.40

'''output------
78.50
31.40
------------'''