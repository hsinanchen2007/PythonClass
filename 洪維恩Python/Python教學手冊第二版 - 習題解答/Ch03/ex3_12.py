# ex3_12.py,
s1 = "Have a nice day"  # 設定字串 s1
print(f"字串 s1 = {s1}")  # 輸出 s1

# (a) 提取出 "nice" 這個子字串
substring = s1[7:11]
print(f"(a) 提取的子字串：{substring}")  # nice

# (b) 判別 "day" 是否有在 s1 內
is_day_in_s1 = "day" in s1
print(f"(b) 判別 'day' 是否在 s1 內：{is_day_in_s1}")  # True

# (c) 提取 s1 的最後一個字元
last_char = s1[-1]
print(f"(c) s1 的最後一個字元：{last_char}")  # y

# (d) 找出 s1 內，字元碼最大的字元
max_char = max(s1)
print(f"(d) 字元碼最大的字元：{max_char}")  # y

'''output-----------------------------
字串 s1 = Have a nice day
(a) 提取的子字串：nice
(b) 判別 'day' 是否在 s1 內：True
(c) s1 的最後一個字元：y
(d) 字元碼最大的字元：y
-----------------------------------'''