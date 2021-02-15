from setting import headers
import re
import requests
from wenben import changebq
from wj import tp

have = 1
url = input('输入url：')
# num = int(input('请输入次数：'))


def findSave(url, ff='w'):
    r = requests.get(url=url, headers=headers)
    text = r.text
    name = re.search('<h4 class="text-center">(.*?)</h4>', text)[1]
    name = name.replace('，', 'd')
    name = name.replace('?', 'w')
    name = name.strip()
    # urls_p = re.search('<span class="last"><em>上一篇:<a href=/(.*?)>', text, re.S)[1]
    urls_n = 0
    urls_n = re.search(
        '<a><em>下一篇:<a href=/(.*?)>', text, re.S)
    # print(urls_n)
    if urls_n is None:
        urls = -1
    else:
        urls = 'http://www.xsxs.xyz/'+urls_n[1]
        # print(urls)
    p = re.search('<div class="panel-body">.*?</h4>(.*?)<nav', text, re.S)[1]
    p = changebq(p)
    # p.encode()
    with open(xs3+name+'.txt', ff, encoding='utf-8')as fp:
        fp.write(p)

    print(name, url, '成功！！！！')
    return urls


for i in range(0, num):
    # print(u)
    # findSave('http://www.huang758.xyz/text/'+u, name)
    url = findSave(url)
    print(have)
    have += 1
    if(url == -1):
        print("\n没有更多了")
        print('......')
        break
print('\nall is OK！！！！！')
