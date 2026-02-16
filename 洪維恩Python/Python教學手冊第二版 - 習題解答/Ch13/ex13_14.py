# ex13_14.py
# 原始網址: https://www.ptt.cc/bbs/food/index.html
import requests
from bs4 import BeautifulSoup
base_url = "https://www.ptt.cc"
current_url = "/bbs/food/index.html"
with open('ch13/ex13_14.txt', 'w', encoding='utf-8') as f:
    n_pages = 5
    for i in range(n_pages):
        f.write(f'第 {i+1} 頁\n')
        url = base_url + current_url
        r = requests.get(url)
        r.encoding = "utf-8"
        sp=BeautifulSoup(r.text, 'html.parser')
        articles = sp.find_all('div', class_='r-ent')   # 找出所有的文章區塊
        for data in articles:
            try:
                title_block = data.find('div', class_='title')  # 找標題
                title_tag =title_block.find('a')            # 找出<a>標籤
                title = title_tag.text.strip()
                meta_tag=data.find('div',class_='meta')  
                author =meta_tag.find('div', class_='author').text    # 作者            
                date=meta_tag.find('div', class_='date').text.strip() # 發文日期                      
                f.write(f'{title}, {author}, {date}\n')   # 寫入檔案
            except:
                title = '本文已被刪除'                 # 沒有<a>，代表文章被刪除
                author = '(無作者資訊)'
                date =  '(無日期資訊)'        
                f.write(f'{title}, {author}, {date}\n')   # 寫入檔案
            
        # 找出上一頁的網址
        btn_group = sp.find('div', class_='btn-group-paging')
        if btn_group:
            prev_page = btn_group.find_all('a')[1]
            if prev_page:
                current_url = prev_page['href']
            else:
                break
print("爬取結果已寫入檔案")

'''output--------------
爬取結果已寫入檔案
--------------------'''