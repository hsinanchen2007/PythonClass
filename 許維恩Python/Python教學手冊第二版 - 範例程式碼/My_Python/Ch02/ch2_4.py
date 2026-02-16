# ch2_4.py, 使用 f-字串格式化輸出的範例
name = 'Bob'
age = 30
height = 175.5
score = 88.456

# 使用 f-string 進行格式化輸出
print(f'Name: {name}')				# 插入字串變數
print(f'Age: {age} years old')			# 插入整數變數
print(f'Height: {height:.1f} cm')		# 浮點數保留 1 位小數
print(f'Score: {score:.2f}')			# 浮點數保留 2 位小數
print(f'Summary: {name} is {age} years old.')	 # 插入多個變數
print(f'{name} is {height:.1f} cm tall.')		 # 格式化身高
print(f'{name}\'s score is {score:.1f} points.')	 # 格式化分數