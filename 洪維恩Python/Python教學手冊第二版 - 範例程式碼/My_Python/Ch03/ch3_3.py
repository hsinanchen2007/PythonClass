# ch3_3.py, 字元的8進位與16進位表示法 
# 換行符號 (16進位的ASCII 碼為 0A)
print('這是一行文字\x0A這是下一行文字')

# 表示版權符號
copyright = '\u00A9'	# Unicode 字元的16進位表示法
print(f'版權符號：{copyright}')

# 表示黑桃符號
spade = '\u2660'	# Unicode 字元的16進位表示法
print(f'黑桃符號：{spade}')