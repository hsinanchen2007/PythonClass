# ch8_4.py, with open() as 的範例
with open('text.txt', 'w', encoding='utf-8') as f:   # 寫檔
    f.write('Python程式設計')  # 將文字寫入檔案
 
with open('text.txt', 'r', encoding='utf-8') as f:  # 讀檔
    print('讀取兩個字元:', f.read(2))
    print('指標位置:', f.tell())
    print('讀取六個字元:', f.read(6))
    print('指標位置:', f.tell())
    f.seek(0)  # 將檔案指標移動到檔案開頭
    print('從頭讀取檔案所有內容:', f.read())