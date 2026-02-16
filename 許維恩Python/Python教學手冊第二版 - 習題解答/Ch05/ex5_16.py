# ex5_16.py
def to_upper(str1=None):    
    if str1 is None:    # 如果 str1 沒有傳入，則返回 'Null'
        return 'Null'  
    result = ""# 初始化一個空字串，將轉換後的字元加到這裡   
    for char in str1:   # 走訪字串中的每個字元        
        if 'a' <= char <= 'z':  # 如果小寫字母，則轉換為大寫
            result += char.upper()
        else:            
            result += char      # 否則保持原來的字元
    return result

# 測試範例
print("to_upper('Julia_program'):", to_upper('Julia_program'))
print("to_upper():", to_upper())

'''output-----------------------------------
to_upper('Julia_program'): JULIA_PROGRAM
to_upper(): Null
-----------------------------------------'''