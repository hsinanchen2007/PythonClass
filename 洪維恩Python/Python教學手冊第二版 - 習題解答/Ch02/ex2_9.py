# ex2_9.py
# 驗證 (a) 8 < 3 and 7 == 9 and 7 > 4
result_a = 8 < 3 and 7 == 9 and 7 > 4
print("(a) Result:", result_a)

# 驗證 (b) 2 > 8 or 7 <= 8 and 7 > 2
result_b = 2 > 8 or 7 <= 8 and 7 > 2
print("(b) Result:", result_b)

# 驗證 (c) 5 > 3 and 4 < 2 or 6 == 6
result_c = 5 > 3 and 4 < 2 or 6 == 6
print("(c) Result:", result_c)

'''output----------
(a) Result: False
(b) Result: True
(c) Result: True
----------------'''

'''說明------------------------------------------------------
每個條件表達式的運算結果：
(a) 8 < 3 and 7 == 9 and 7 > 4
    8 < 3：這是 False，因為 8 不是小於 3。
    7 == 9：這是 False，因為 7 不是等於 9。
    7 > 4：這是 True，因為 7 是大於 4。
    在 and 運算中，只要有一個條件是 False，整個結果就會是 False。
    所以這個表達式的結果是 False。
(b) 2 > 8 or 7 <= 8 and 7 > 2
    2 > 8：這是 False，因為 2 不是大於 8。
    7 <= 8：這是 True，因為 7 是小於或等於 8。
    7 > 2：這是 True，因為 7 是大於 2。
    在 or 運算中，只要有一個條件是 True，整個結果就會是 True。
    因此，這個表達式的結果是 True。
(c) 5 > 3 and 4 < 2 or 6 == 6
    5 > 3：這是 True，因為 5 是大於 3。
    4 < 2：這是 False，因為 4 不是小於 2。
    6 == 6：這是 True，因為 6 等於 6。
    由於 and 的優先級高於 or，所以會先計算 5 > 3 and 4 < 2，
    這個結果是 False，然後再進行 False or 6 == 6，
    最終結果是 True。
------------------------------------------------------------'''