# ex5_28.py
# (a) 定義函數 rgb2gray(r, g, b)
def rgb2gray(r, g, b):
    """將紅色 r、綠色 g 和藍色 b 轉成灰階 v，並四捨五入到整數"""
    return round(r * 0.299 + g * 0.587 + b * 0.114)

print("(a) 定義函數 rgb2gray(r, g, b) 已完成")

# (b) 計算 lst=[32,56,128] 的灰階值
lst = [32, 56, 128]
gray_value = rgb2gray(*lst)  # 使用解包運算子 *

print(f"(b) lst = {lst} 的灰階值為: {gray_value}")

# (c) 計算 colors 裡每個子串列的灰階值
colors = [[34, 128, 34], [56, 22, 169], [147, 43, 98], [155, 65, 38]]
gray_values = [rgb2gray(*color) for color in colors]  # 使用串列生成式

print(f"(c) colors 裡每個子串列的灰階值為: {gray_values}")

'''output---------------------------------------------
(a) 定義函數 rgb2gray(r, g, b) 已完成
(b) lst = [32, 56, 128] 的灰階值為: 57
(c) colors 裡每個子串列的灰階值為: [89, 49, 80, 89]
---------------------------------------------------'''