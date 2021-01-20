import requests
from lxml import etree
import os
url = 'http://pic.netbian.com/4kdongman/'
headers = {
    'User-Argent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
# response.encoding = 'gbk'
response.encoding = response.apparent_encoding
page_text = response.text
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
if not os.path.exists('./text/pics'):
    os.mkdir('./text/pics')
for li in li_list:
    img_src = 'http://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
    # print(img_name, img_src)
    img_data = requests.get(url=img_src, headers=headers).content
    img_path = './text/pics/'+img_name
    with open(img_path, 'wb')as fp:
        fp.write(img_data)
        print(img_name, '下载成功！！！')
