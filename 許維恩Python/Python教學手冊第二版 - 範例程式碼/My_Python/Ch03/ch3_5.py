# ch3_5.py, 檢查是否為有效的郵件地址
email = input('請輸入電子郵件地址：')
email = email.lower()  # 將字串轉換為小寫

# 檢查是否包含 '@' 且以 '.com' 結尾，並輸出True或False
print('@' in email and email.endswith('.com'))