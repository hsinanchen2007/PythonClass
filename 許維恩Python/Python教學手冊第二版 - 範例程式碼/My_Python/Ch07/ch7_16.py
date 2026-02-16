# ch7_16.py, 傳統程式語言的getter和setter
class Circle:
    def __init__(self, r):
        self.set_radius(r)				# 呼叫setter
    def get_radius(self):  			# getter，用來獲取半徑
        return self._rad
    def set_radius(self, r):   			# setter，用來設置半徑
        self._rad = r if r > 0 else 0
    def area(self):					# area() 函數
        return 3.14 * self._rad ** 2

c1 = Circle(5)
print('Radius:', c1.get_radius())		# 呼叫getter
print('Area:', c1.area()) 				# 計算圓面積

c1.set_radius(-10)  					# 呼叫 setter
print('New Radius:', c1.get_radius())
print('New Area:', c1.area())