# ch7_6.py, 檢查e-mail的格式-使用靜態函數
class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    @staticmethod				# 靜態函數
    def check(email):  		# 確認 Email 裡有 '@'
        return '正確的email' if '@' in email else '錯誤的email'

print(Student.check('invalid-email'))		# 錯誤的email
s1 = Student('Alice', 'alice@email.com')	# 建立Student物件
print(Student.check(s1.email)) 			# 正確的email