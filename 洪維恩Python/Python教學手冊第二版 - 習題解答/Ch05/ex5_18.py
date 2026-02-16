# ex5_18.py
# (a) 定義全域變數 counter，初始值為 0
# 定義函數 increment()，每次被呼叫時將 counter 的值加 1
counter = 0
def increment():
    global counter  # 使用全域變數 counter
    counter += 1

# (b) 定義函數 get_counter()，回傳 counter 的當前值
def get_counter():
    return counter

# (c) 在主程式中，呼叫 increment() 三次，然後呼叫 get_counter()，並印出結果
increment()
increment()
increment()
print(get_counter())  # 呼叫 get_counter() 並印出結果

'''output--------------------
3
--------------------------'''