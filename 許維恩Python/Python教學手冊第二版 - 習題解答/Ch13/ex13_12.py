# ex13_12.py
import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/food/index.html"
req = requests.get(url)
req.encoding = "utf-8"
sp=BeautifulSoup(req.text, "html.parser")

articles = sp.find_all('div',class_='r-ent')            # 找出所有的文章區塊
for data in articles:    
    try: 
        title_block = data.find('div', class_='title')  # 找標題     
        title_tag =title_block.find('a')                # 找出<a>標籤
        if title_tag.text.startswith("[食記]"):
            title = title_tag.text.strip()      # 找出[食記]開頭的標題
            print(f'{title}') 
    except:
        title = '本文已被刪除'                           # 文章被刪除
        print(f'{title}')                               # 列印標題

'''output---------------------------------------
[食記] 楊梅 首烏客家海鮮~五訪貓人私房菜
[食記] 新竹東區 涓豆腐(新竹巨城店)
[食記] 新竹將軍村裡的咖啡早午餐日常 日出咖啡
[食記] 新北中和寶媽乾拌麵 鹹香餛飩麵
[食記] 沖繩那霸 JAM'S TACOS 國際通店 塔可飯
[食記] 海鮮長谷川 日本宮崎 伊勢龍蝦湯海鮮丼飯
[食記] 高雄 Falling in 啡煙 高人氣美味甜點店
[食記] 嘉義 民主火雞肉飯
[食記] 日本福岡-會動的烏賊生魚片-河太郎
[食記] 釜山 廣安人氣面海韓食餐廳-Nasari食堂
[食記] 北海道拉麵魚貝和雞 台北大安 濃牡蠣拉麵
[食記] 台中 丸南生魚片 搬新家近逢甲夜市$10/片
[食記] 高雄 鄧師傅功夫菜-中正總店
[食記] 台中 豐原區｜蘿娜印度廚坊
[食記] 新竹縣竹北市。阿中丸子
[食記] 基隆市中正區-要塞司令部洋食廚房
[食記] 台南可頌控必朝聖！美味儀式LE BAKER
---------------------------------------------'''