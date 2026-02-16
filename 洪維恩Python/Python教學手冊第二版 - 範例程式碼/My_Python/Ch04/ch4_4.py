# ch4_4.py, 判別一個數是正數、0或是負數
num = int(input('請輸入一個整數：'))

if num > 0:
    print('您輸入的是正數')
elif num < 0:
    print('您輸入的是負數')
else:
    print('您輸入的是零')