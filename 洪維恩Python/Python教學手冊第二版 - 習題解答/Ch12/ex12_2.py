# ex12_2.py
import pandas as pd
d0 = {'Apple': 25, 'Orange': 36, 'Pineapple': 62}    # 建立字典 d0
s = pd.Series(d0)   # 建立 Series 物件 s

# (a) 提取價格大於50的品項
a_result = s[s > 50]
print("(a) 價格大於50的品項：")
print(a_result)

# (b) 計算 Apple 和 Orange 價錢的總和
b_result = s['Apple'] + s['Orange']
print("\n(b) Apple 和 Orange 價錢總和：")
print(b_result)

# (c) 以指定索引建立 Series s2
s2 = pd.Series(d0, index=['Orange', 'Kiwi', 'Apple'])
print("\n(c) 指定索引建立的 s2：")
print(s2)

# (d) 將缺失值補為30，儲存為 s3
s3 = s2.fillna(30)
print("\n(d) 將缺失值補為30後的 s3：")
print(s3)

# (e) 捨棄 s3 中的缺失值
e_result = s3.dropna()
print("\n(e) 捨棄缺失值後的結果：")
print(e_result)

# (f) 計算 s3 與 s 的加總
f_result = s3 + s
print("\n(f) s3 與 s 的加總結果：")
print(f_result)

# 找出值為 NaN 的品項
nan_items = f_result[f_result.isna()]
print("值為 NaN 的品項：")
print(nan_items)

'''output-------------------------
(a) 價格大於50的品項：
Pineapple    62
dtype: int64

(b) Apple 和 Orange 價錢總和：
61

(c) 指定索引建立的 s2：
Orange    36.0
Kiwi       NaN
Apple     25.0
dtype: float64

(d) 將缺失值補為30後的 s3：
Orange    36.0
Kiwi      30.0
Apple     25.0
dtype: float64

(e) 捨棄缺失值後的結果：
Orange    36.0
Kiwi      30.0
Apple     25.0
dtype: float64

(f) s3 與 s 的加總結果：
Apple        50.0
Kiwi          NaN
Orange       72.0
Pineapple     NaN
dtype: float64
值為 NaN 的品項：
Kiwi        NaN
Pineapple   NaN
dtype: float64
-------------------------------'''

'''說明-----------------------------------------------
(f)有哪些品項的值為NaN？為什麼會得到NaN這個結果？
s3 + s 是「索引對齊」相加，Kiwi 不存在於 s，
Pineapple 不存在於 s3，所以它們對應位置的值會是 NaN。
--------------------------------------------------'''