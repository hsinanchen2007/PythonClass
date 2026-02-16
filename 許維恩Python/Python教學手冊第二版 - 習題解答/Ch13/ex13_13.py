# ex13_13.py
# 原始網址: https://www.ptt.cc/bbs/food/index.html
import requests
from bs4 import BeautifulSoup
base_url = "https://www.ptt.cc"
current_url = "/bbs/food/index.html"
with open('ch13/ex13_13.txt', 'w', encoding='utf-8') as f:
    n_pages = 5
    for i in range(n_pages):
        f.write(f'第 {i+1} 頁\n')
        url = base_url + current_url
        req = requests.get(url)
        req.encoding = "utf-8"
        sp=BeautifulSoup(req.text, 'html.parser')
        articles = sp.find_all('div',class_='r-ent')        # 找出所有的文章區塊
        for data in articles:
            try:
                title_block = data.find('div', class_='title')  # 找標題
                title_tag =title_block.find('a')            # 找出<a>標籤
                if title_tag.text.startswith("[食記]"):
                    title = title_tag.text.strip()
                    f.write(f'{title}\n')   
            except:
                title = '本文已被刪除'                 # 沒有<a>，代表文章被刪除
                f.write(f'{title}\n')               # 寫入檔案  
        # 找出上一頁的網址
        btn_group = sp.find('div', class_='btn-group-paging')
        if btn_group:
            prev_page = btn_group.find_all('a')[1]
            if prev_page:
                current_url = prev_page['href']
            else:
                break
print("爬取結果已寫入檔案")

'''output---------------------------------------
爬取結果已寫入檔案
---------------------------------------------'''