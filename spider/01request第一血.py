import requests
# 1指定url
url = 'https://www.sogo.com/'
# 2发起请求
response = requests.get(url=url)
# 3获取响应数据
page_text = response.text
print(page_text)
# 4持久化存储
with open('./text/sogo.html', 'w', encoding='utf-8')as fp:
    fp.write(page_text)

print('ok')
