# ch4_23.py, 檢查輸入的串列是否有負數（for-else的寫法）
lst=eval(input('請輸入一個串列: '))
for n in lst:
    if n<0:
        print('找到負數')
        break
else:
    print('都是正數')