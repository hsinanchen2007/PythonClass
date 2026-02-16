# ex11_2.py
import numpy as np
import matplotlib.pyplot as plt
# 建立子圖（2列2欄，共4個圖）
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# (a) f(x) = x^4 + 6x^3 + 7x + 3, -7 ≤ x ≤ 4
x1 = np.linspace(-7, 4, 400)
y1 = x1**4 + 6*x1**3 + 7*x1 + 3
axes[0, 0].plot(x1, y1, color='blue')
axes[0, 0].set_title('(a) $f(x) = x^4 + 6x^3 + 7x + 3$')
axes[0, 0].grid(True)

# (b) f(x) = sin(x^2)cos(x), -π ≤ x ≤ π
x2 = np.linspace(-np.pi, np.pi, 400)
y2 = np.sin(x2**2) * np.cos(x2)
axes[0, 1].plot(x2, y2, color='green')
axes[0, 1].set_title('(b) $f(x) = \\sin(x^2)\\cos(x)$')
axes[0, 1].grid(True)

# (c) f(x) = e^(-0.5x) sin(x), 0 ≤ x ≤ 4π
x3 = np.linspace(0, 4*np.pi, 400)
y3 = np.exp(-0.5*x3) * np.sin(x3)
axes[1, 0].plot(x3, y3, color='red')
axes[1, 0].set_title('(c) $f(x) = e^{-0.5x} \\sin(x)$')
axes[1, 0].grid(True)

# (d) y(t) = e^(-t) sin(3t+2), 0 ≤ t ≤ 2π
t = np.linspace(0, 2*np.pi, 400)
y4 = np.exp(-t) * np.sin(3*t + 2)
axes[1, 1].plot(t, y4, color='purple')
axes[1, 1].set_title('(d) $y(t) = e^{-t} \\sin(3t+2)$')
axes[1, 1].grid(True)

# 自動調整圖與圖之間的距離
plt.tight_layout()
plt.show()

'''output-----

-----------'''