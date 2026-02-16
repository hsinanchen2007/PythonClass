# ch6_6.py, 判別兩句話的相似度
text1 = 'The quick brown fox jumps over the lazy dog'
text2 = 'A quick brown fox jumps above a lazy dog'

stopwords = {'the', 'a', 'over', 'above'}   # 停用詞集合
s1 = set(text1.split())	# 將句子分成單字，再轉集合（含停用詞）
s2 = set(text2.split())

s1c = s1 - stopwords		# 去除停用詞， - 為差集運算
s2c = s2 - stopwords		# 去除停用詞

# 計算 Jaccard 相似度
sim_raw = len(s1 & s2) / len(s1 | s2)		 # & 為交集，| 為聯集
sim_clean = len(s1c & s2c) / len(s1c | s2c)

print(f'原始相似度（含停用詞）：{sim_raw:.2f}')
print(f'去除停用詞後相似度：{sim_clean:.2f}')
