# ch7_15.py, 訂正ch7_14的錯誤
class Parent:
    def __init__(self):
        self.__value = 10  	# 使用雙底線，讓屬性變為私有
    def get_value(self):
        return self.__value  	# 存取私有屬性

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = 20  		# 這個value變成了 Child 自己屬性

p = Parent()
c = Child()
print(p.get_value())  		# 10
print(c.get_value())  		# 10（Child 無法覆蓋Parent的 __value）