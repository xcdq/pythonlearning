import requests
url = 'https://pic.qiushibaike.com/system/pictures/12399/123993126/medium/36W02ABMMX77OFEW.jpg'
# text字符串 content二进制 json()
img_data = requests.get(url=url).content
with open('./text/qiutu.jpg', 'wb')as fp:
    fp.write(img_data)
