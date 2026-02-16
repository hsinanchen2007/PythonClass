# ch2_5.py, input() 函數的使用範例
name = input('Enter name: ')  			 # 輸入姓名
age = int(input('Enter age: '))		 # 輸入年齡並轉換為整數
height = float(input('Enter height: '))	 # 輸入身高並轉換為浮點數

print(f'Name: {name}')
print(f'Age: {age} years old')
print(f'Height: {height:.2f} cm')