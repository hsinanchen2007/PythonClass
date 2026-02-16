# ex4_24.py
text = "machine_learning"   # 字串
index = 0   # 設定索引

# 使用while迴圈尋找第一個不是英文字母的字元
while index < len(text) and text[index].isalpha():
    index += 1

# 輸出結果
print(f"位於索引{index}")

'''output-------------
位於索引7
-------------------'''