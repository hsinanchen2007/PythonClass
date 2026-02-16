# ch11_9.py, 更改取樣點的數目並加入畫布名（含中文字型設定）
import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0, 2*np.pi, 36)
x2 = np.linspace(0, 2*np.pi, 128)

with plt.rc_context({'font.family': 'Microsoft JhengHei',
                     'axes.unicode_minus': False}):
    fig, ax = plt.subplots(2, 1, figsize=(12, 4))
    fig.suptitle('不同的取樣點數', fontsize=16)  		# 中文標題
    ax[0].plot(x1, np.sin(x1**2))
    ax[1].plot(x2, np.sin(x2**2), 'r')
    fig.subplots_adjust(hspace=0.4)
    plt.show()