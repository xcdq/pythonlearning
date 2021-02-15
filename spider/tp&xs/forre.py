import re
url = 'https://wx4.sinaimg.cn/orj360/006WNXJOly1gdc9c5m28hj30rs92qx6p.jpg'
name = re.search('/([^/]*)$', url)[1]
print(name)
