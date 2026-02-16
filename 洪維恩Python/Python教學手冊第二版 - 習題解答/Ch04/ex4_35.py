# ex4_35.py
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']  # 季節名稱列表

# 取出所有母音並組成新的字元串列
vowels = [ch for word in seasons for ch in word if ch.lower() in "aeiou"]
print(vowels)   # 印出結果

'''output----------------------------------
['i', 'u', 'e', 'A', 'u', 'u', 'i', 'e']
----------------------------------------'''