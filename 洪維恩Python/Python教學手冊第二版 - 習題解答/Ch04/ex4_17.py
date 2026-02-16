# ex4_17.py
print("圖案 (a):")
for i in range(1, 6):
    for j in range(6 - i, 6):
        print(j, end="")
    print()
print()

print("圖案 (b):")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

print("圖案 (c):")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(i, end="")
    print()
print()

print("圖案 (d):")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
print()

print("圖案 (e):")
for i in range(0, 6):
    print(str(6 - i) * i)
print()

print("圖案 (f):")
for i in range(5, 0, -1):  # 控制列數
    print(" " * (5 - i), end="")  # 印出前面的空格
    for j in range(1, i + 1):  # 印出數字
        print(j, end="")
    print()  # 換行
print()

print("圖案 (g):")
for i in range(5, 0, -1):
    print(" " * (5 - i), end="")  # 印出前面的空格
    for j in range(5, 5 - i, -1):  # 從5到i印數字
        print(j, end="")
    print()  # 換行
print()

print("圖案 (h):")
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(6 - i, 6):
        print(j, end="")
    print()

'''output-------------------------
圖案 (a):
5
45
345
2345
12345

圖案 (b):
12345
1234
123
12
1

圖案 (c):
55555
4444
333
22
1

圖案 (d):
54321
4321
321
21
1

圖案 (e):

5
44
333
2222
11111

圖案 (f):
12345
 1234
  123
   12
    1

圖案 (g):
54321
 5432
  543
   54
    5

圖案 (h):
    5
   45
  345
 2345
12345
-------------------------------'''