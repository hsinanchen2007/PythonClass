# ex5_11.py
def square(tpl):
    # 回傳每個數字的平方
    return [x ** 2 for x in tpl]

# 範例使用
result = square([2, 4, 6])
print(result)  # 輸出: [4, 16, 36]

'''output--------------------
[4, 16, 36]
--------------------------'''