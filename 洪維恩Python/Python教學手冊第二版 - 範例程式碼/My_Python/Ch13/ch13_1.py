# ch13_1.py, 發送GET請求
import requests				# 載入套件
url = 'https://www.udn.com'	# 目標網站
req = requests.get(url) 		# 發送GET請求
if req.status_code == 200:    	# 狀態碼200 表示請求成功
    print('GET請求成功！')    	# 印出請求成功
    print(req.text[:41])		# 印出回應的HTML內容前41字
else:
    print(f'請求失敗！狀態碼:{req.status_code}')