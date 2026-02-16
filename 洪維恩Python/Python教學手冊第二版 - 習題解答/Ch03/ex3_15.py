# ex3_15.py
s = '*^_^* Python *w_w*'
# 刪除 '*' 符號及其他字符，只保留 'Python'
s1 = s.replace('*^_^*', '')
result=s1.replace('*w_w*', '').strip()
print(result)  # 輸出：Python

'''output----------
Python
----------------'''