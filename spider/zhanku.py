from lxml import etree
import requests
import os
import re
# url = 'https://www.zcool.com.cn/work/ZNTAzNzY5ODQ=.html'
# url = 'https://www.zcool.com.cn/work/ZNDg3MTY0MDA=.html'
# url = 'https://www.zcool.com.cn/work/ZMzIxMjM0NDQ=.html'
url = input()
src = re.search('work/(.*)=\.html', url)[1]


def make_dir(src):
    """文件夹创建"""
    if not os.path.exists('./text/MN/'+src):
        os.makedirs('./text/MN/'+src)


def make_save(src, pic, data):
    """保存图片"""
    img_name = re.search('community/(.*?)@', pic)[1]
    # print(img_name)
    img_path = './text/MN/'+src+"/"+img_name
    with open(img_path, 'wb')as fp:
        fp.write(img_data)
        print(img_name, '下载成功！！！')


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
pic_list = tree.xpath(
    '//*[@id="body"]/main//div[@class="photo-information-content"]/img/@src')
# print(page_text)
# print(page_text.type)
src = re.search('h2>(.*?)<span', page_text, re.S)[1].strip()
print(src)
make_dir(src)
for pic in pic_list:
    img_data = requests.get(url=pic, headers=headers).content
    make_save(src, pic, img_data)
    # print(pic)
print('下载完成')
