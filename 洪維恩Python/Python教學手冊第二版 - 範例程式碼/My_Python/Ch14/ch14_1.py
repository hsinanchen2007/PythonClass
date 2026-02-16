# ch14_1.py, imread() 與 imshow() 的練習
import imageio.v3 as iio
import matplotlib.pyplot as plt

# 讀取圖檔（注意檔案路徑）
img = iio.imread('ch14/img01.jpg')   

# 顯示圖像
plt.imshow(img)		# 顯示圖像
plt.axis('off')  	# 不顯示座標軸
plt.show()			# 顯示圖像視窗