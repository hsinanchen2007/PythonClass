# ex3_19.py
items = []  # 初始化空串列

# (a) 將 "筆記本" 加入串列
items.append("筆記本")
print(f"(a) {items}")

# (b) 將 "鉛筆" 加入串列開頭
items.insert(0, "鉛筆")
print(f"(b) {items}")

# (c) 在 "筆記本" 之後插入 "橡皮擦"
index = items.index("筆記本") + 1
items.insert(index, "橡皮擦")
print(f"(c) {items}")

'''output--------------------------
(a) ['筆記本']
(b) ['鉛筆', '筆記本']
(c) ['鉛筆', '筆記本', '橡皮擦']
--------------------------------'''