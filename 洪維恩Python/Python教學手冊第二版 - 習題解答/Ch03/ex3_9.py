# ex3_9.py
# 以林美麗為例
# (a) 直接使用 Unicode 控制碼輸出 "林美麗"
print("(a) \u6797\u7F8E\u9E97")     # 印出查詢對應林美麗的unicode碼

# (b) 16 進位 Unicode 轉換成 10 進位
unicode_lin = int("6797", 16)
unicode_mei = int("7F8E", 16)
unicode_li = int("9E97", 16)
print(f"(b) {unicode_lin}, {unicode_mei}, {unicode_li}")

# (c) 使用 ord() 取得 Unicode 編碼
ord_lin = ord('林')  
ord_mei = ord('美')
ord_li = ord('麗')
print(f"(c) {ord_lin}, {ord_mei}, {ord_li}")

# (d) 將 10 進位 Unicode 轉回 16 進位字串格式
char_lin = chr(ord_lin)     # 轉換回「林」
char_mei = chr(ord_mei)     # 轉換回「美」
char_li = chr(ord_li)       # 轉換回「麗」 
print(f"(d) {char_lin}{char_mei}{char_li}")  # 輸出結果

'''output--------------------
(a) 林美麗
(b) 26519, 32654, 40599
(c) 26519, 32654, 40599
(d) 林美麗
--------------------------'''