# ch8_12.py, 加入異常處理的程式，濾掉無法轉成int的輸入
while True:
    n=input('Input a number:')
    if n in 'Qq':
        print('Quit program')
        break
    try: 
        print(int(n)**2)		# 這行可能會出錯
    except Exception:			# 這行可接收拋出的任何異常
        print('Input error')