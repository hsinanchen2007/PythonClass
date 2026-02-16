# ch7_5.py, 簡單的學生管理系統
class Student:
    count = 0   # 類別屬性，用於計數，由所有物件共享
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1			# 每次建立物件時計數增加
    @classmethod					# 類別函數from_age()
    def from_age(cls, name, age):
        return cls(name, age)		# 直接傳回類別的物件
    @classmethod					# 類別函數get_count()
    def get_count(cls):
        return cls.count  			# 傳回目前的物件數量

print(f'total: {Student.get_count()}')
s1 = Student('Alice', 20)			# 建立物件
s2 = Student.from_age('Bob', 22)  	# 使用類別函數建立物件
print(f'Name: {s1.name}, Age: {s1.age}')
print(f'Name: {s2.name}, Age: {s2.age}')
print(f'total: {Student.get_count()}')	# 由類別呼叫get_count()
print(f'total: {s1.get_count()}')		# 由物件呼叫get_count()