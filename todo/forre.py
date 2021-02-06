import re
# txt = 'https://img.zcool.cn/community/019d71600966ed11013e399161bbc5.jpg@1280w_1l_0o_100sh.jpg'
# # all = re.search('community/(.*?)@', txt)[1]
# print(all)
# txt = " <h2>     遇萤 <span"
# all = re.search('h2>(.*)<span', txt)[1].strip()
# print('a', all, 'a')
url = "<li><a href='view-4124-6.html'>6</a></li><li><a href='view-4124-7.html'>7</a></li>"
# pic = re.search('(.*?\.jpg)', url)[1]
# pic = re.search('community/(.*)', url)[1]
# print(pic)
urls = re.findall('<li><a href=\'(.*?)\'', url, re.S)
# findSave(url, name)
for u in urls:
    print(u)
