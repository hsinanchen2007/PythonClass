# ch13_8.py, 取得5頁文章標題、連結
# ch13_8.py, 取得5頁文章標題、連結
import requests
from bs4 import BeautifulSoup
base_url = 'https://www.ptt.cc'     # PTT主網域名稱
current_url = '/bbs/pet/index.html' # 當前頁面的路徑
with open('ch13/ch13_8.txt', 'w', encoding='utf-8') as f:
    f.write('文章標題, 連結\n')    
    n_pages = 5     # 要爬取的頁數
    for i in range(n_pages):
        f.write(f'第{i+1}頁\n')
        url = base_url + current_url  # 取得當前頁面的完整網址
        req = requests.get(url)
        sp = BeautifulSoup(req.text, 'html.parser')
        # 找出所有的文章區塊
        articles = sp.find_all('div',class_='r-ent')        
        for data in articles:
            try:
                title_block = data.find('div', class_='title') 
                title_tag =title_block.find('a')	# 找<a>標籤
                title = title_tag.text.strip()  	# 找標題
                link = base_url + title_tag['href'] 	# 文章連結                
                f.write(f"{title}, {link}\n")       	# 寫入檔案
            except:
                title = '本文已被刪除'
                f.write(f"{title}\n")       # 寫入檔案
        # 找出上頁連結
        btn_group = sp.find('div', class_='btn-group-paging')
        if btn_group:    # 如果有找到按鈕群組
            prev_page = btn_group.find_all('a')[1]
            if prev_page: # 如果有找到上一頁按鈕
                current_url = prev_page['href'] # 更新current_url
            else:
                break
        else:
            break
print("爬取結果已存入檔案中")