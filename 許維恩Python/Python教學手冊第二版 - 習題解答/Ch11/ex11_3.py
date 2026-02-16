# ex11_3.py
import numpy as np
import matplotlib.pyplot as plt
# 建立 x 值與對應的 y 值
x = np.linspace(0, 4 * np.pi, 400)
y = np.sin(x) / (x + 1)

# 繪製圖形
plt.figure(figsize=(8, 4))
plt.plot(x, y, label=r'$f(x) = \dfrac{\sin(x)}{x+1}$', color='teal')
plt.title('f(x) = sin(x)/(x+1)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

plt.savefig('Ch11/ex11_3.png', dpi=72, transparent=False)   # 儲存圖形，dpi=72，背景不透明
plt.show()  # 顯示圖形

'''output------------------------------

------------------------------------'''