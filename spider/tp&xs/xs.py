import requests
import re
url = input('输入url：')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}


def findSave(url, name, ff='a'):
    r = requests.get(url=url, headers=headers)
    text = r.text
    p = re.search('<div class="pt-3">(.*?)</div>', text, re.S)[1]
    p = p.replace('<br/>', '\n')
    p = p.replace('</p>', '\n')
    p = p.replace('<p>', '')
    p = p.replace('&nbsp;', '')
    p.encode()
    with open('./text/txt/'+name+'.txt', ff, encoding='utf-8')as fp:
        fp.write(p)
    print(url, '成功！！！！')


r = requests.get(url=url, headers=headers).text
name = re.search('<h4>(.*?)</h4>', r)[1]
urls = re.findall('<li><a href=\'(.*?)\'', r, re.S)
findSave(url, name, ff='w')
for u in urls:
    print(u)
    findSave('http://www.huang758.xyz/text/'+u, name)
print(name, 'OK')
