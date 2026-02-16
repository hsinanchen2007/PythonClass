# ch7_17.py, 使用 @property撰寫getter和setter
class Circle:
    def __init__(self, r):
        self.radius = r    		# 這一行會呼叫setter

    @property     				# 使用@property定義getter
    def radius(self):			# 把函數名稱radius當屬性來用
        print('getter 被呼叫了')
        return self._rad

    @radius.setter 			# 使用@radius.setter定義setter
    def radius(self, r):		# 函數名稱應和getter相同
        print('setter 被呼叫了')
        self._rad = r if r > 0 else 0

    def area(self):     		# 計算圓形的面積
        return 3.14 * self._rad ** 2

c1= Circle(5)
print('Radius:', c1.radius)		# 呼叫 getter
print('Area:', c1.area())    		# 呼叫 area()
c1.radius = -10  					# 呼叫 setter
print('New Radius:', c1.radius)	# 呼叫 getter
print('New Area:', c1.area())		# 呼叫 area()
