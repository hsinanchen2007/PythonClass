# ch13_5.py, 取得文章標題
import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/pet/index.html'
req = requests.get(url)
req.encoding = 'utf-8'
sp = BeautifulSoup(req.text, 'html.parser')

articles = sp.find_all('div', class_='r-ent')# 找出所有的文章區塊
for data in articles:
    try:
        title_block = data.find('div', class_='title')  # 找標題
        title_tag = title_block.find('a')
        title = title_tag.text.strip()
    except:
        title = '本文已被刪除'
    print(title)