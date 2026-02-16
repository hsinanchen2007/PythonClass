# ch7_9.py, 帶有__init__() 的繼承範例
class Phone:  # 父類別，手機
    def __init__(self, brand):
        self.brand = brand			# 手機品牌

class Smartphone(Phone):			# 子類別，智慧型手機
    def __init__(self, brand, os):
        super().__init__(brand)	# 呼叫父類別的 __init__()
        self.os = os  				# 智慧型手機的操作系統屬性
    def info(self):
        return f'{self.brand} 智慧型手機，操作系統: {self.os}'

my_phone = Smartphone('Apple', 'iOS')  # 建立子類別的物件
print(my_phone.info())