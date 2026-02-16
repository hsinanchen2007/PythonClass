# ch8_3.py, readline() 和readlines() 函數
file = open('Ch08//demo.txt', 'r', encoding='utf-8')  # 開啟檔案

# readline() 一次讀取一行，讀取到\n即停止，strip()可去除\n
print('readline():', file.readline().strip())  # 讀取第一行
print('readline():', file.readline().strip())  # 讀取第二行
 
# readlines() 一次讀取多行，回傳一個包含所有行的串列
print('readlines():', file.readlines())  # 讀取剩餘所有行，回傳串列
file.close()  # 關閉檔案