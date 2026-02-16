# ch4_12.py, 九九乘法表
for r in range(1, 6):  # 外層迴圈，控制乘數
    for c in range(1, 9): # 內層迴圈，控制被乘數
        print(f'{r}*{c}={r * c:2d}', end=' ')
    print()  # 換行，開始印下一列