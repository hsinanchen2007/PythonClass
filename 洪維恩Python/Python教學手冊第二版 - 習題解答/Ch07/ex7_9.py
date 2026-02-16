# ex7_9.py
class Student:
    student_count = 0  # 類別屬性 student_count，初始值為 0

    def __init__(self, name):
        self.name = name  # 實例屬性 name，學生姓名
        Student.student_count += 1  # 每建立一個新學生，學生總數自動遞增

    @classmethod
    def get_student_count(cls):
        return cls.student_count  # 傳回目前的學生總數

# 測試
s1 = Student('Alice')
s2 = Student('Bob')
s3 = Student('Charlie')

print(Student.get_student_count())  # 輸出: 3

'''output--------------------
3
--------------------------'''