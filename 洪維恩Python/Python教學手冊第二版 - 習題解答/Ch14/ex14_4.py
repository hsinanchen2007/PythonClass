# ex14_4.py
import matplotlib.pyplot as plt
from skimage import data

# 讀取並處理圖像
man = data.camera()
man[man > 150] = 150

# 繪製
plt.imshow(man, cmap='gray', vmin=0, vmax=150)
plt.title('camera limited to 150')
plt.axis('off')
plt.show()

'''output-----------------------------------------

-----------------------------------------------'''