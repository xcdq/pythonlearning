from lxml import etree
from wj import tp
import requests
import os
import re
# url = 'https://www.zcool.com.cn/work/ZNTAzNzY5ODQ=.html'
# url = 'https://www.zcool.com.cn/work/ZNDg3MTY0MDA=.html'
# url = 'https://www.zcool.com.cn/work/ZMzIxMjM0NDQ=.html'
url = input('请输入链接：')
dx = input('图片质量（低：1、高：2）：')
# src = re.search('work/(.*)=\.html', url)[1]
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}


def make_dir(page_text, dx):
    """文件夹创建"""
    src = re.search('h2>(.*?)<', page_text, re.S)[1].strip()
    src = src.replace('|', '')
    src += ('（高）')if dx == '2' else ('（低）')
    print(src)
    if not os.path.exists(tp+src):
        os.makedirs(tp+src)
    return src


def make_save(src, pic):
    """保存图片"""
    img_data = requests.get(url=pic, headers=headers).content
    img_name = re.search('community/(.*?.jpg)', pic)[1]
    # print(img_name)
    img_path = tp+src+"/"+img_name
    with open(img_path, 'wb')as fp:
        fp.write(img_data)
        print(img_name, '下载成功！！！')


page_text = requests.get(url=url, headers=headers).text
# with open('./text/zk.html', 'w') as fb:
#     fb.write(page_text)
tree = etree.HTML(page_text)
pic_list = tree.xpath(
    '//*[@id="body"]/main//div[@class="photo-information-content"]/img/@src')
src = make_dir(page_text, dx)
for pic in pic_list:
    if(dx == '2'):
        pic = re.search('(.*?\.jpg)', pic)[1]
    print(pic)

    make_save(src, pic)
    # print(pic)
print('下载完成')
