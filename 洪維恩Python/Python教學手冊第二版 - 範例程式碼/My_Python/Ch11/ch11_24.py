# ch11_24.py, 長條圖 
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,10)
fig, ax = plt.subplots()
ax.bar(x, np.sin(x), color='yellow', width=0.8, edgecolor= 'blue')
plt.show()