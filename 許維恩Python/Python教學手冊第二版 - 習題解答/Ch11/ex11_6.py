# ex11_6.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, np.pi, 400)      # 建立 x 值
# 計算兩個函數
y1 = np.sin(x**2)
y2 = np.sin(x)**2

# 繪圖
plt.figure(figsize=(8, 4))
plt.plot(x, y1, label=r'$f_1(x) = \sin(x^2)$', color='blue')
plt.plot(x, y2, label=r'$f_2(x) = \sin^2(x)$', color='orange')

# 加上標題與座標軸標籤
plt.title('$f_1(x) = \\sin(x^2)$ & $f_2(x) = \\sin^2(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

plt.legend(loc='lower left')  # 加上圖例，放在左下角
plt.show()  # 顯示圖形

'''output----

----------'''