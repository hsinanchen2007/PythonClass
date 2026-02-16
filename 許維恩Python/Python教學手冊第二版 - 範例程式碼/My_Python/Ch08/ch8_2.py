# ch8_2.py, 附加內容到已存在檔案後面
file = open('demo.txt', 'a', encoding='utf-8')  # 附加模式
file.write('如傳世的青花瓷自顧自美麗，\n')  # 使用 write() 寫入單行
file.write('妳眼帶笑意。\n')
file.close()  		# 關閉檔案
 
file = open('demo.txt', 'r', encoding='utf-8')  # 讀取模式
print(file.read())  	# read() 讀取檔案全部內容，含換行符號
file.close()  # 關閉檔案
