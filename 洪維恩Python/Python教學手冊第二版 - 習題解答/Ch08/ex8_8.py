# ex8_8.py
try:
    # 嘗試使用 'utf-8' 解碼
    result = b'\x04\xeb\x12'.decode('utf-8')
except UnicodeDecodeError:
    # 捕捉到解碼錯誤時，印出錯誤訊息
    print('utf-8解碼錯誤')

'''output---------
utf-8解碼錯誤
---------------'''