# ch8_11.py, 未經異常處理的程式
while True:
    n = input('Input a number:')
    if n in 'Qq':					# 如果n為'Q'或'qq'
        print('Quit program')
        break
    else:							# 否則印出n的平方
        print(int(n)**2)