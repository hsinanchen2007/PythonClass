# ch5_9.py,傳遞不可變物件到函數
def modify_string(s):
    s1 = 'Hello'          # 字串 'Hello' 會從駐留池取得
    s2 = 'Python'         # 字串 'Python' 會新建
    print(f'函數中s的id: {id(s)}, s1的id: {id(s1)}')

    s = s1 + ' ' + s2   # 嘗試修改s，實際上會建立新的字串
    print('修改後的字串s:', s)
    print('修改後的s的id:', id(s))
    return s

# 主程式
str1 = 'Hello'
str2 = modify_string(str1)   # 呼叫函數
print(f'主程式中str1的id: {id(str1)}, str2的id: {id(str2)}')
print('主程式中str2的值:', str2)