# ex5_8.py
def to_numbers(word):
    word = word.upper()  # 轉為大寫，統一處理
    result = ""
    for char in word:
        if char.isdigit():  # 處理數字
            result += char
        elif char in 'ABC': result += '2'
        elif char in 'DEF': result += '3'
        elif char in 'GHI': result += '4'
        elif char in 'JKL': result += '5'
        elif char in 'MNO': result += '6'
        elif char in 'PQRS': result += '7'
        elif char in 'TUV': result += '8'
        elif char in 'WXYZ': result += '9'
    return result

# 測試範例
word = "PYTHON"
print(word, '=', to_numbers(word))

'''output--------------------
PYTHON = 798466
--------------------------'''