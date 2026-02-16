# ch13_2.py, 取得各種標籤的內容
import requests
from bs4 import BeautifulSoup
url = 'https://wienhong.github.io/cats.html'
req = requests.get(url)
req.encoding = 'utf-8'
sp = BeautifulSoup(req.text, 'html.parser')
print(sp.title.text.strip())	# 列印<title>標籤的內容
print(sp.h1.text.strip())		# 列印<h1>標籤的內容
print(sp.p.text.strip())		# 列印<p>標籤的內容
print(sp.a.text.strip())		# 列印<a>標籤的內容