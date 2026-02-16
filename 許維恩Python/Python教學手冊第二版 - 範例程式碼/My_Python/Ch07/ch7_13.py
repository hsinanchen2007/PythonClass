# ch7_13.py, 前綴為單底線的屬性
class Example:
    def __init__(self):
        self._data = 42	# 單底線表示這是內部使用的屬性
    def show_data(self):
        print(f'內部資料: {self._data}')

obj = Example()
obj.show_data()  			# 正常存取
print(obj._data)  		# 雖然可以存取，但按照慣例不建議這樣做
obj._data = 100  			# 仍然可以修改，但不建議這樣直接更改
obj.show_data()  			# 確認修改後的值