# ex14_13.py
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import astronaut
from skimage.color import rgb2hsv, hsv2rgb

# 讀取圖像並轉為浮點數格式（0~1）
astro = astronaut()
astro_float = astro / 255.0

# (a) RGB → HSV → uint8
astro_hsv = rgb2hsv(astro_float)
astro_hsv_uint8 = (astro_hsv * 255).astype(np.uint8)

# (b) HSV → RGB → uint8
# 注意：要先將 astro_hsv 再轉回 0~1 範圍再轉回 RGB
astro_hsv_back = astro_hsv_uint8 / 255.0
astro_rgb = (hsv2rgb(astro_hsv_back) * 255).astype(np.uint8)

# (c) 顯示 astro 與 astro_rgb
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(astro)
plt.title("Original astro")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(astro_rgb)
plt.title("RGB after HSV roundtrip")
plt.axis('off')

plt.tight_layout()
plt.show()

# (d) 比較三個通道的像素差異
diff_map = astro != astro_rgb  # shape = (512, 512, 3)

# 顯示每個通道的差異（相同為黑，不同為白）
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
channels = ['Red Channel', 'Green Channel', 'Blue Channel']

for i in range(3):
    axs[i].imshow(diff_map[:, :, i], cmap='gray')
    axs[i].set_title(f"(d) Difference - {channels[i]}")
    axs[i].axis('off')

plt.tight_layout()
plt.show()

'''output-----

-----------'''