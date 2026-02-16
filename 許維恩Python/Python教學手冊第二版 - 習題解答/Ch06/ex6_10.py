# ex6_10.py
def find_value(tpl, target):
    index = 0                       # 從索引 0 開始
    while index < len(tpl):
        if tpl[index] == target:    # 如果當前元素等於目標值
            return index            # 回傳該索引
        index += 1                  # 否則繼續查找下個元素
    return -1                       # 如果沒找到，回傳 -1

# 測試範例
tpl = (10, 20, 30, 40)
target = 30
print(find_value(tpl, target))      # 輸出應為 2

'''output----
2
----------'''