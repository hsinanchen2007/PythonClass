# ch14_9.py, 圖像的切割 
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

man = data.camera()
manP = man.reshape(8,64,8,64).swapaxes(1, 2)   # 切割圖像

fig,ax = plt.subplots(8,8,figsize = (5, 5))
for r in range(8):
    for c in range(8):
        ax[r,c].imshow(manP[r,c],cmap = 'gray')
        ax[r,c].axis('off')

fig.subplots_adjust(wspace = 0.1)  		# 水平間距為子圖寬度的0.1
fig.subplots_adjust(hspace = 0.1)  		# 垂直間距為子圖高度的0.1
plt.show()