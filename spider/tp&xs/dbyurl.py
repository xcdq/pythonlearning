# from setting import headers
# import requests
import re
import tool
from save_in import save_tp, keep_tp
from wj import tp
import time

temp = 0
url = input('url: ')
txt = tool.get_txt(url, 'utf-8')
# print(txt)
img_urls = re.findall('<p.*?><img src="(.*?)" /></p>', txt)
# img_urls = re.findall('"img":"(.*?)"', txt)

name = re.search('<h1.*?>(.*?)<', txt, re.S)[1].strip()
name = name.replace('|', '')
# name = name.replace('+', '')
# name = name.replace(',', '')
# name=name.replace('|','')

# name = 'hello'
print(name)
for img_url in img_urls:
    print(img_url)
    # img_url = 'http://imgoss.cnu.cc/'+img_url
    keep_tp(tp, 'gulin//'+name+'//', '', img_url)
    temp += 1
