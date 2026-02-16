# ex5_2.py
def pow(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result
x=2; n=3
print(x,'的',n,'次方 =',pow(x, n))  # 輸出 8

'''output--------------------
2 的 3 次方 = 8
--------------------------'''