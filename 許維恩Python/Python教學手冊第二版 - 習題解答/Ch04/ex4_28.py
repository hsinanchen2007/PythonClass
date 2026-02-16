# ex4_28.py
count = 0
n = 1

while True:
    if n % 3 == 2 and n % 5 == 3 and n % 7 == 2:
        print(n, end=' ')
        count += 1
    n += 1
    if count == 3:
        break  # 當找到3個解時，終止迴圈

'''output--------------------
23 128 233 
--------------------------'''