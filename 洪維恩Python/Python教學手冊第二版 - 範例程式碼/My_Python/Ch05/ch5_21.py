# ch5_21.py, zip() 和 enumerate() 函數的應用
names = ['Alice', 'Bob', 'Jenny']   	# 學生的名字
math = [85, 90, 78]   					# 數學成績
english = [88, 92, 80]   				# 英文成績

# 使用 zip 函數將學生的名字與他們的成績配對，並計算總成績
results = []
for name, ma, en in zip(names, math, english):
    total = ma + en
    results.append((name, total)) 
print('學生的總成績:', results) 

# 利用enumerate() 印出序號和學生資訊
for i, (name, total) in enumerate(results, start=1):
    print(f'{i}: {name}，總成績: {total}')