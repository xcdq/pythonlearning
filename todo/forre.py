import re
# txt = 'https://img.zcool.cn/community/019d71600966ed11013e399161bbc5.jpg@1280w_1l_0o_100sh.jpg'
# # all = re.search('community/(.*?)@', txt)[1]
# print(all)
# txt = " <h2>     遇萤 <span"
# all = re.search('h2>(.*)<span', txt)[1].strip()
# print('a', all, 'a')
url = 'https://img.zcool.cn/community/0137735fb3c7b311013ee04dc09f8f.jpg'
# pic = re.search('(.*?\.jpg)', url)[1]
pic = re.search('community/(.*)', url)[1]
print(pic)