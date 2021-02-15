import requests
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Argent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
page_text = requests.get(url=url, headers=headers, proxies={
                         "http": '113.194.128.238:9999'}).text
with open('./text/ip.html', 'w', encoding='utf-8')as fp:
    fp.write(page_text)
