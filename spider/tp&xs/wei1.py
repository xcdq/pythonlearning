from setting import headers
import requests
import re
from save_in import save_tp, keep_tp
from wj import tp
url = input('输入url：')
uu = re.findall('(.*?)\.html', url)[0]
# print(uu)


def get_txt(url):
    r = requests.get(url=url, headers=headers)
    r.encoding = 'gbk'
    txt = r.text
    return txt


# txt.encode(r.encoding)
# print(txt)
# 页数
txt = get_txt(url)
# print(re.findall('<a>共(.*)页: </a>', txt, re.S))
if re.findall('<a>共(.*)页: </a>', txt, re.S) == []:
    # print('ok')
    name = re.findall('<img alt="(.*?)" src="', txt, re.S)[0]
    name = name.replace('"', ' ')
    name = name.strip()

    img_url = re.findall('<img alt=".*?" src="(.*?)" />', txt, re.S)[0]
    keep_tp(tp, name, name+'.jpg', img_url)
else:
    num = int(re.findall('<a>共(.*)页: </a>', txt, re.S)[0])
    print('共'+str(num)+'张\n现在开始下载：')
    # 名字
    name = re.findall('<img alt="(.*?)" src="', txt, re.S)[0]
    name = name.replace('"', ' ')
    name = name.strip()

    img_url = re.findall('<img alt=".*?" src="(.*?)" />', txt, re.S)[0]
    # print(r.encoding)
    # print(img_url)
    keep_tp(tp, name, name+'1.jpg', img_url)
    for i in range(2, num+1):

        txt = get_txt(uu+"_"+str(i)+".html")
        img_url = re.findall('<img alt=".*?" src="(.*?)" />', txt, re.S)[0]
        save_tp(tp+name, name+str(i)+".jpg", img_url)
    print('OK')
