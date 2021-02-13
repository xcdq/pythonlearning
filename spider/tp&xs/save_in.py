from wj import *
import os
import requests
from setting import headers


def keep_tp(path, drname, name, data_url):
    # drname.replace('"', ' ')
    path = path+drname
    if not os.path.exists(path):
        os.makedirs(path)
    save_tp(path, name, data_url)


def save_tp(path, name, data_url, ff='wb'):
    path += '/'
    data = requests.get(url=data_url, headers=headers).content
    with open(path+name, ff)as fp:
        fp.write(data)
        print(name, '下载成功')
