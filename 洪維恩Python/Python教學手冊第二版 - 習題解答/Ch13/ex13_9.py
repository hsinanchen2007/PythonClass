# ex13_9.py
# 原始網址: https://wienhong.github.io/ex13_8.html
import requests
from bs4 import BeautifulSoup
url = "https://wienhong.github.io/ex13_8.html"
base_url = "https://wienhong.github.io/"
r = requests.get(url)
r.encoding = "utf-8"
sp=BeautifulSoup(r.text, "html.parser")

# 取得所有圖片的網址
images = sp.find_all("img")
for image in images:
    img_url = base_url + image["src"]
    if not img_url.startswith("http"):
        img_url = base_url + img_url
    print(f'圖片網址： {img_url}')

# 取得所有連結的網址
links = sp.find_all("a")
for link in links:
    href = link.get("href")    
    if href:
        print(f'超連結網址： {href}')

'''output---------------------------------------------------
圖片網址： https://wienhong.github.io/ex13_8_collie.jpg
圖片網址： https://wienhong.github.io/ex13_8_labrador.jpg
超連結網址： https://zh.wikipedia.org/wiki/%E7%8B%97
超連結網址： https://www.doctordog.org.tw/
---------------------------------------------------------'''