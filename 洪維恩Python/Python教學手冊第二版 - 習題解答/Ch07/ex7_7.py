# ex7_7.py
class Employee:
    company = 'Unknown'  # 類別屬性 company，初始值為 'Unknown'

    def __init__(self, name, salary):
        self.name = name  # 實例屬性 name，員工姓名
        self.salary = salary  # 實例屬性 salary，員工薪水

    def display_info(self):
        print(f"姓名: {self.name}, 薪水: {self.salary}, 公司: {Employee.company}")

# 測試
Employee.company = 'TechCorp'  # 設定公司名稱為 'TechCorp'

emp1 = Employee('Alice', 50000)
emp2 = Employee('Bob', 60000)

emp1.display_info()  # 輸出: 姓名: Alice, 薪水: 50000, 公司: TechCorp
emp2.display_info()  # 輸出: 姓名: Bob, 薪水: 60000, 公司: TechCorp

'''output----------------------------------
姓名: Alice, 薪水: 50000, 公司: TechCorp
姓名: Bob, 薪水: 60000, 公司: TechCorp
----------------------------------------'''