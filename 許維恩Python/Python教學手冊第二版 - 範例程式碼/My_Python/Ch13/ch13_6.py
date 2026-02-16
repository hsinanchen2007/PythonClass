# ch13_6.py, 取得文章標題、作者、發文日期
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
        title_tag =title_block.find('a')     # 找出<a>標籤                           
        title = title_tag.text.strip()                        
        meta_tag=data.find('div',class_='meta')# 找作者和發文日期
        author =meta_tag.find('div', class_='author').text            
        date=meta_tag.find('div', class_='date').text.strip()
        print(f'{title}, {author}, {date}')   # 列印結果
    except:
        title = '本文已被刪除'
        print(title)   	                     # 列印結果