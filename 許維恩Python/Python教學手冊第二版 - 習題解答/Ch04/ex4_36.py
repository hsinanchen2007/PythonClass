# ex4_36.py
# 單字列表
words = ['State', 'University', 'of', 'New', 'York', 'at', 'Buffalo']

# 找出包含 'a' 的單字
words_with_a = [word for word in words if 'a' in word.lower()]
print(words_with_a) # 印出結果

'''output--------------------
['State', 'at', 'Buffalo']
--------------------------'''