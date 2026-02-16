# ch13_4.py, 取得圖片完整的URL
import requests
from bs4 import BeautifulSoup
url = 'https://wienhong.github.io/cats.html'
base_url = 'https://wienhong.github.io/'
req = requests.get(url)
req.encoding = 'utf-8'
sp = BeautifulSoup(req.text, 'html.parser')

# 找出所有的<img>標籤
images = sp.find_all('img')     		# 找出所有的<img>標籤
for img in images:
    img_url = img.get('src')    		# 取得圖片的 URL
    if not img_url.startswith('http'):  # 若不是完整的URL
        img_url = base_url + img_url  	# 加上網域名稱
    print(f'圖片網址: {img_url}')