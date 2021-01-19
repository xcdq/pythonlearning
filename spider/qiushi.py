import requests
import re
import os
url = 'https://www.qiushibaike.com/imgrank/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
if not os.path.exists('./text/qiutuLibs'):
    os.makedirs('./text/qiutuLibs')
page_text = requests.get(url=url, headers=headers).text
ex = '<div class="thumb">.*?<img src="(.*?)".*?</div>'
img_src_list = re.findall(ex, page_text, re.S)
# print(img_src_list)
for src in img_src_list:
    src = 'https:'+src
    imgData = requests.get(url=src, headers=headers).content
    # 图片名称
    img_name = src.split('/')[-1]
    imgPath = './text/qiutuLibs/'+img_name
    with open(imgPath, 'wb')as fp:
        fp.write(imgData)
        print(img_name, '下载成功！！！！')
