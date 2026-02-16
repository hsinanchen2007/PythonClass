# ex8_12.py,
def to_byteArray(lst):
    try:
        # 印出將要轉換的內容
        print("正在轉換的內容:", lst)        
        # 將每個整數轉換為 bytes，並生成 bytes 物件
        byte_array = bytes(lst)
        return byte_array
    except (TypeError, ValueError, OverflowError) as e:
        # 若出現錯誤，顯示錯誤訊息
        print("無法轉換")
        return None

# 測試函數
lst1 = [65, 66, 67]  # 正常的整數串列
lst2 = [300, 256]    # 超過單字節範圍的整數
lst3 = [1.5, 2.5]    # 含有浮點數的串列

print(to_byteArray(lst1),'\n')
print(to_byteArray(lst2),'\n')
print(to_byteArray(lst3))

'''output-----------------------------
正在轉換的內容: [65, 66, 67]
b'ABC' 

正在轉換的內容: [300, 256]
無法轉換
None

正在轉換的內容: [1.5, 2.5]
無法轉換
None
-----------------------------------'''