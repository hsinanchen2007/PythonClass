# ex7_16.py
# 定義 Person 類別
class Person:
    def __init__(self, name):
        self.name = name  # 設定姓名屬性

    def print_name(self):
        print(self.name)  # 輸出姓名

# 定義 Student 類別，繼承自 Person
class Student(Person):
    def __init__(self, name, gender):
        super().__init__(name)  # 呼叫父類別的 __init__() 設定 name 屬性
        self.gender = gender  # 設定性別屬性

    def print_info(self):
        print(f'{self.name}, {self.gender}')  # 輸出姓名和性別

# 測試
student = Student('Bob', 'Male')
student.print_info()  # 輸出: Bob, Male

'''output------
Bob, Male
------------'''