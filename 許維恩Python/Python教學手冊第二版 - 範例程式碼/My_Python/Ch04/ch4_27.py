# ch4_27.py, 將兩個字串的字母轉成大寫
words = ['hi', ' hello']
chars = [c.upper() for word in words  for c in word]
print(''.join(chars))