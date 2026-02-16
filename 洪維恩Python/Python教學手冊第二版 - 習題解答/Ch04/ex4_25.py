# ex4_25.py
print("不能被3整除有", end="")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")

'''output--------------------
不能被3整除有 1 2 4 5 7 8 10
--------------------------'''