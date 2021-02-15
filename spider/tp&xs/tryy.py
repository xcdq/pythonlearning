import requests
from tool import get_txt
# 1指定url
url = input('输入测试url：')
# 2发起请求
response = get_txt(url, 'utf-8')
# 3获取响应数据
# page_text = response.text
print(response)
# 4持久化存储
with open('hello.html', 'w', encoding='utf-8')as fp:
    fp.write(response)

print('ok')
