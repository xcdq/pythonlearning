from wj import xs
from wenben import changebq
import requests
import re
have = 1
url = input('输入url：')
num = int(input('请输入次数：'))
# print(num)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}


def findSave(url, ff='w'):
    r = requests.get(url=url, headers=headers)
    text = r.text
    name = re.search('<h3 st.*?>(.*?)</h3>', text)[1]
    name = name.replace('，', 'd')
    name = name.replace('?', 'w')
    name = name.strip()
    # urls_p = re.search('<span class="last"><em>上一篇:<a href=/(.*?)>', text, re.S)[1]
    urls_n = 0
    urls_n = re.search(
        '<span class="next"><em>下一篇:<a href=/(.*?)>', text, re.S)
    # print(urls_n)
    if urls_n is None:
        urls = -1
    else:
        urls = 'http://www.qqc98.xyz/'+urls_n[1]
        # print(urls)
    p = re.search('<div class="novelContent">(.*?)</div>', text, re.S)[1]
    p = changebq(p)
    # p.encode()
    with open(xs+name+'.txt', ff, encoding='utf-8')as fp:
        fp.write(p)

    print(name, url, '成功！！！！')
    return urls


# r = requests.get(url=url, headers=headers).text
# findSave(url, name, ff='w')
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
