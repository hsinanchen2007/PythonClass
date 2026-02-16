# ch6_7.py, 計算單字出現的次數
count = {}  # 初始化一個空字典
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 使用 setdefault 函數來計算每個單字出現的次數
for word in words:
    count.setdefault(word, 0)
    count[word] += 1

print(count) 