# ex13_8.py
# 原始網址: https://wienhong.github.io/ex13_8.html
import requests
from bs4 import BeautifulSoup
url = "https://wienhong.github.io/ex13_8.html"
r = requests.get(url)
r.encoding = "utf-8"
sp=BeautifulSoup(r.text, "html.parser")
print(sp.title.text)
print(sp.h2.text)
print(sp.p.text.strip())

'''output----------
狗狗世界
狗狗相片
狗是人類最忠誠的朋友，充滿活力，樂於陪伴主人，並能擔任 多種任務，如搜救和輔助治療。
----------------'''