# ex5_7.py
def bin2dec(bs):
    if len(bs) == 0:
        return None  # 空字串回傳 None
    
    decimal = 0
    power = 0  # 追蹤次方數
    for digit in reversed(bs):  # 反轉字串，從最低位開始計算
        if digit not in '01':  
            return None  # 遇到非 0 或 1 的字元則回傳 None
        decimal += int(digit) * (2 ** power)  # 計算加總
        power += 1  # 更新次方數
    return decimal

# 測試
print('1011轉成10進位整數=', bin2dec('1011'))
print('11001轉成10進位整數=', bin2dec('11001'))

'''output--------------------
1011轉成10進位整數= 11
11001轉成10進位整數= 25
--------------------------'''