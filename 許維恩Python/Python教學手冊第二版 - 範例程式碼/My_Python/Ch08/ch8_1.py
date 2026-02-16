# ch8_1.py, 寫入檔案練習
file = open('demo.txt', 'w', encoding='utf-8')  # 開啟檔案

# 使用 write() 寫入單行
file.write('天青色等煙雨，')  
file.write('而我在等妳。\n')

# 使用 writelines() 一次寫入多個字串
file.writelines(['月色被打撈起，', '暈開了結局。\n'])
file.close() 		# 關閉檔案