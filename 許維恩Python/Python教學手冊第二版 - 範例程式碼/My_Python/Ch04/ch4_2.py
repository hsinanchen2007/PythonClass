# ch4_2.py, 檢查手機號碼格式 
num = input('請輸入手機號碼（格式：09xx-xxx-xxx）：')

if num[:2] == '09' and num[4] == '-' and num[8] == '-':
    print('格式正確')
    print(f'您輸入的號碼為 {num:s}') 
else:
    print('格式錯誤')