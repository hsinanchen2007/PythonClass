# ch7_14.py, 子類別覆蓋父類別屬性的範例
class Parent:
    def __init__(self):
        self.value = 10		# 沒有使用雙底線，子類別可能會覆蓋它
    def get_value(self): 		# 傳回value的值
        return self.value  		

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = 20  		# 直接覆蓋了父類別的value

p = Parent()
c = Child()
print(p.get_value())  		# 10（父類別的屬性正常）
print(c.get_value())  		# 20（子類別的屬性覆蓋了父類別的value）