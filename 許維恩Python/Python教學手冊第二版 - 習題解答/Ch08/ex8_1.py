# ex8_1.py
# (a) 將 'Python' 寫入純文字檔 ex8_1.txt
with open('Ch08\\ex8_1.txt', 'w', encoding='utf-8') as f:
    f.write('Python')

# (b) 開啟 ex8_1.txt，逐字元讀取並加入串列 lst
lst = []
with open('Ch08\\ex8_1.txt', 'r', encoding='utf-8') as f:
    while True:
        ch = f.read(1)  # 一次讀取一個字元
        if ch == '':    # 如果是空字串，代表檔案讀完了
            break
        lst.append(ch)

print(lst)  # 顯示結果

'''output--------------------------
['P', 'y', 't', 'h', 'o', 'n']
--------------------------------'''