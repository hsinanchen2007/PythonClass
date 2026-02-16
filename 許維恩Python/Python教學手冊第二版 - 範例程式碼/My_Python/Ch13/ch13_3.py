# ch13_3.py, 取得圖片和超連結網址
import requests
from bs4 import BeautifulSoup
url = 'https://wienhong.github.io/cats.html'
req = requests.get(url)
req.encoding = 'utf-8'
sp = BeautifulSoup(req.text, 'html.parser')

# 找出所有的<img>標籤
images = sp.find_all('img') 	# 找出所有的<img>標籤
for img in images:
    img_url = img.get('src')  	# 取得圖片的 URL
    print(f'圖片網址: {img_url}')

# 爬取並列印所有超連結的網址
links = sp.find_all('a')  		# 找到所有 <a> 標籤
for link in links:
    href = link.get('href')  	# 取得超連結的 URL
    if href:  				# 檢查是否有 href 屬性
        print(f'超連結網址: {href}')  	# 列印超連結的 URL