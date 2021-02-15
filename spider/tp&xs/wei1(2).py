from setting import headers
import requests
import re
from save_in import save_tp, keep_tp
from wj import tp
import time
urls = []
temp = 0
tp = tp+"唯一图库\\"
f = open("E:\\OneDrive - stu.hebut.edu.cn\\vscode\\Python\\spider\\tp&xs\\tp.txt")
url = f.readline()
num = 1
while url:

    url = url.strip()
# for i in range(0, 10):
#     strr = '输入url  '+str(i)+' ：'
#     url = input(strr)
#     urls.append(url)
# for url in urls:

    print('第', temp, '次下载开始')
    temp += 1
    time.sleep(1.2)
    print(url)
    uu = re.findall('(.*?)\.html', url)[0]
    name_uu = re.findall('/(\d*?)\.html', url)[0]

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
        # print(name_uu)
        name = name.replace('"', ' ')
        name = name.strip()
        name = name_uu+name

        img_url = re.findall('<img alt=".*?" src="(.*?)" />', txt, re.S)[0]
        keep_tp(tp, name, name+'.jpg', img_url)
    else:
        num = int(re.findall('<a>共(.*)页: </a>', txt, re.S)[0])
        print('共'+str(num)+'张\n现在开始下载：')
        # 名字
        name = re.findall('<img alt="(.*?)" src="', txt, re.S)[0]
        name = name.replace('"', ' ')
        name = name.strip()
        name = name_uu+name

        img_url = re.findall('<img alt=".*?" src="(.*?)" />', txt, re.S)[0]
        # print(r.encoding)
        # print(img_url)
        keep_tp(tp, name, name+'1.jpg', img_url)
        for i in range(2, num+1):

            txt = get_txt(uu+"_"+str(i)+".html")
            img_url = re.findall('<img alt=".*?" src="(.*?)" />', txt, re.S)[0]
            save_tp(tp+name, name+str(i)+".jpg", img_url)
        print('OK')
    url = f.readline()
