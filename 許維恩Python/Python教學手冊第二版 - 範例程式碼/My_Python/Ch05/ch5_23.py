# ch5_23.py, 亂數產生器的實作
def toy_lcg(seed, a=5, c=1, m=16):	# 線性同餘亂數產生器 (LCG)
    while True:
        seed = (a * seed + c) % m
        yield seed					# 傳回新的亂數

# 使用範例
lcg = toy_lcg(seed = 3)			# 初始化亂數產生器，種子值為 3
print(next(lcg)) 					# 產生一個亂數
print(next(lcg)) 					# 產生一個亂數
for _ in range(20):  				# 產生 20 個亂數
    print(next(lcg), end = ' ') 