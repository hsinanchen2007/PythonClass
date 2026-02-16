# ch5_7.py, 不可變物件的建立與駐留機制 
# 測試短字串的駐留機制
s1 = 'apple'
s2 = 'apple'
print(f's1 的 id: {id(s1)}, s2 的 id: {id(s2)}')

# 測試重新設值
s2 = 'banana'
s3 = s2
print(f's2 的 id: {id(s2)}, s3 的 id: {id(s3)}')