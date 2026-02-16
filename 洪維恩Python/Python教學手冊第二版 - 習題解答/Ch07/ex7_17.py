# ex7_17.py
class Student:
    def __init__(self, name, age):
        self.set_name(name)  # 設置姓名
        self.set_age(age)  # 設置年齡

    def set_name(self, name):
        self._name = name  # 設置姓名

    def set_age(self, age):
        if self.validate_age(age):
            self._age = age  # 設置年齡
        else:
            print("無效的年齡")  # 若年齡無效，顯示錯誤訊息

    def validate_age(self, age):
        return 18 <= age <= 25  # 檢查年齡是否在有效範圍內

    def get_info(self):
        return f"{self._name}, {self._age} years old"  # 返回學生資訊

# 測試
student = Student('Alice', 20)
print(student.get_info())  # 輸出: Alice, 20 years old
student.set_age(150)  # 輸出: 無效的年齡

'''output-------------
Alice, 20 years old
無效的年齡
-------------------'''