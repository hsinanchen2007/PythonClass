# ex7_14.py
# 定義父類別 Shape
class Shape:
    def area(self):
        pass  # 父類別的 area 方法沒有具體實作

# 定義矩形子類別 Rectangle，繼承自 Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # 計算矩形面積

# 定義圓形子類別 Circle，繼承自 Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * (self.radius ** 2),2)  # 計算圓形面積

# 測試
rect = Rectangle(4, 5)
circle = Circle(3)
print(rect.area())   # 預期輸出: 20
print(circle.area()) # 預期輸出: 28.27

'''output------
20
28.27
------------'''