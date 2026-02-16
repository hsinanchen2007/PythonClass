# ex3_13.py,
s1 = "it is never too late to learn"    # 設定字串 s1

# (a) 將 s1 的每一個單字的第一個字母轉換成大寫
capitalized_words = s1.title()
print(f"(a) 每個單字的第一個字母轉換成大寫：{capitalized_words}")

# (b) 將 s1 的第一個字母轉換成大寫
first_letter_capitalized = s1.capitalize()
print(f"(b) 第一個字母轉換成大寫：{first_letter_capitalized}")

# (c) 測試 s1 是否全為英文字母
is_alpha = s1.isalpha()  # 去除空格後，檢查是否全為字母
print(f"(c) s1 是否全為英文字母：{is_alpha}")

# (d) 計算字元 "e" 在 s1 中出現的次數
e_count = s1.count('e')
print(f"(d) 字元 'e' 在 s1 中出現的次數：{e_count}")

# (e) 刪除 "never" 這個單字
s1_without_never = s1.replace("never", "")  # 去除 "never"
s1_without_extra_spaces = ' '.join(s1_without_never.split())
print(f"(e) 刪除 'never' 之後的字串：{s1_without_extra_spaces}")

# (f) 把 "late" 換成 "LATE"
s1_with_LATE = s1.replace("late", "LATE")
print(f"(f) 把 'late' 換成 'LATE'：{s1_with_LATE}")

'''output-----------------------------------------------------------
(a) 每個單字的第一個字母轉換成大寫：It Is Never Too Late To Learn
(b) 第一個字母轉換成大寫：It is never too late to learn
(c) s1 是否全為英文字母：False
(d) 字元 'e' 在 s1 中出現的次數：4
(e) 刪除 'never' 之後的字串：it is too late to learn
(f) 把 'late' 換成 'LATE'：it is never too LATE to learn
-----------------------------------------------------------------'''