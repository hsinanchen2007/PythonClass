# ch4_19.py, 利用break跳離無窮迴圈
while True:  
    cmd = input("請輸入指令 (輸入 'exit' 結束): ")  
    if cmd == 'exit':  
        print('程式已結束')  
        break        # 跳離while迴圈
    print(f'你輸入的是: {cmd}')  