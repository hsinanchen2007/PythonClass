# ex11_8.py
import numpy as np
import matplotlib.pyplot as plt

# 避免 x=0 導致 0^0 或 log(0) 的問題，從一個非常小的正數開始
x = np.linspace(0.001, 16, 400)
y = np.power(x, x)

# 建立圖形
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='teal', label=r'$y = x^x$')

plt.yscale('log') # 設定 y 軸為對數尺度

# 標題與標籤
plt.title('y = x^x')
plt.xlabel('x')
plt.ylabel('y (log scale)')
plt.grid(True, which='both')  # 顯示主次網格線
plt.legend()

plt.show()# 顯示圖形

'''output----

----------'''