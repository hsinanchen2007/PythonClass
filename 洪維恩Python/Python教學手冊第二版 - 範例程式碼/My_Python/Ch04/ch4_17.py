# ch4_17.py, 搜尋字元
text = 'Hello, world!'
target = ','		# 欲搜尋的字元

for ch in text:
    if ch == target:
        print('找到字元:', target)
        break     # 找到字元，終止迴圈
    print('目前字元:', ch)