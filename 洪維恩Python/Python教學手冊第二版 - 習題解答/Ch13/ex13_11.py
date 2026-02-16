# ex13_11.py
# 原始網址: https://wienhong.github.io/cats.html
import requests
url = "https://wienhong.github.io/cats_Mi.jpg"
r = requests.get(url)
r.encoding = "utf-8"
with open("ch13/ex13_11.jpg", "wb") as f:
    f.write(r.content)
print("下載圖片完成")

'''output----------
下載圖片完成
----------------'''