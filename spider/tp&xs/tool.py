import requests
from setting import headers


def get_txt(url, coding='gbk'):
    r = requests.get(url=url, headers=headers)
    r.encoding = coding
    txt = r.text
    return txt
