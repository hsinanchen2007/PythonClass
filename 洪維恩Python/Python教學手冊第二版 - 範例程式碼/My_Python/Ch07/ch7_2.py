# ch7_2.py, 計算圓面積與周長, 類別的寫法
class Circle:
    def __init__(self, rad=1):	# 初始化函數
        self.radius = rad
    def area(self):			# 圓面積函數			
        return 3.14 * self.radius ** 2
    def perimeter(self): 		# 圓周長函數
        return 2 * 3.14 * self.radius

c1 = Circle(4)		# 建立Circle 物件 c1
c2 = Circle()			# 建立Circle 物件 c2
print(f'半徑: {c1.radius}, 面積: {c1.area()}, 周長: {c1.perimeter()}')
print(f'半徑: {c2.radius}, 面積: {c2.area()}, 周長: {c2.perimeter()}')