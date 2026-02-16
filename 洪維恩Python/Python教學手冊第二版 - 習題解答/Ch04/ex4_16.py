# ex4_16.py
print("圖案 (a):")
for i in range(5, 0, -1):
    print('*' * i)
print()

print("圖案 (b):")
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)
print()

print("圖案 (c):")
for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * i)
print()

print("圖案 (d):")
for i in range(5):
    print('^' * i + '*' * (5 - i))
print()

print("圖案 (e):")
for i in range(1, 6):
    print(''.join(str(x) for x in range(1, i + 1)))
print()

print("圖案 (f):")
for i in range(5, 0, -1):  # 控制起始數字從5開始
    for j in range(5, i-1, -1):  # 控制每行的數字，從5減少到當前i
        print(j, end="")  # 印出數字
    print()  # 換行
print()

print("圖案 (g):")
for i in range(1, 6):
    print(str(i) * i)
print()

print("圖案 (h):")
start_char = 0  # 起始數字
for i in range(1, 6):
    line = ''
    for j in range(i):
        if start_char < 10:
            line += str(start_char)  # 數字範圍
        else:
            line += chr(start_char + 87)  # 'a'是ASCII 97，所以要加上87
        start_char += 1
    print(line)

'''output-------------------------
圖案 (a):
*****
****
***
**
*

圖案 (b):
    *
   **
  ***
 ****
*****

圖案 (c):
*****
 ****
  ***
   **
    *

圖案 (d):
*****
^****
^^***
^^^**
^^^^*

圖案 (e):
1
12
123
1234
12345

圖案 (f):
54321
5432
543
54
5

圖案 (g):
1
22
333
4444
55555

圖案 (h):
0
12
345
6789
abcde
-------------------------------'''