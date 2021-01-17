import requests
import json
post_url = 'https://fanyi.baidu.com/sug'
word = input('enter a word  ')
data = {
    'kw': word
}
headers = {
    'User-Argent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
response = requests.post(url=post_url, data=data)
dic_obj = response.json()
# print(dic_obj)
file_name = word+'.json'
fp = open('./'+file_name, 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp)
