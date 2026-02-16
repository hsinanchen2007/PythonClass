# ex5_9.py
def n_digits(num):
    return len(str(abs(num)))  # 使用 abs() 處理負數情況

# 測試範例
n=5591
print(n,'的位數有',n_digits(n),'位')
n=-123
print(n,'的位數有',n_digits(n),'位')

'''output--------------------
5591 的位數有 4 位
-123 的位數有 3 位
--------------------------'''