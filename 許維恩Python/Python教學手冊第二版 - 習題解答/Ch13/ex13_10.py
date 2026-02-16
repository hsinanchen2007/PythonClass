# ex13_10.py
# 原始網址: https://data.gov.tw/dataset/38130
import requests
url = "https://data.moa.gov.tw/service/opendata/BgipTrfiPhenoRecords.aspx?FOTT=CSV&IsTransData=1&UnitId=710"
r = requests.get(url)
r.encoding = "utf-8"
with open("ch13/ex13_10.csv", "w", encoding="utf-8") as f:
    f.write(r.text)
print("下載「台北植物園園區植栽花期紀錄資料集」完成")

'''output-------------------------------------
下載「台北植物園園區植栽花期紀錄資料集」完成
-------------------------------------------'''