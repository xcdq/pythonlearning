# UA请求载体的身份标识
# ua检测与ua伪装

import requests
url = 'https://www.sogou.com/web'
# 处理url携带参数，封装到字典中
kw = input('enter a word ')
param = {
    'query': kw
}
headers = {
    'User-Argent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
response = requests.get(url=url, params=param)
page_text = response.text
fileName = kw+'.html'
with open('./text/'+fileName, 'w', encoding='utf-8')as fp:
    fp.write(page_text)
print('ok')
