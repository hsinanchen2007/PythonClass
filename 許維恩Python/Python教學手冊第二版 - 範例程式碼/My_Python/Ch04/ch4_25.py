# ch4_25.py, 找出輸入數字的所有因數
n = int(input('請輸入一個數字: '))
# 使用 for 迴圈找出因數
factors_for = []
for i in range(1, n+1):
    if n % i == 0:   # 找到因數
        factors_for.append(i)
print(f'{n} 的因數有 (for 迴圈):', factors_for)

# 使用串列推導式找出因數
factors_list_comp = [i for i in range(1, n+1) if n % i == 0]
print(f'{n} 的因數有 (串列推導式):', factors_list_comp)