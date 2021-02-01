import json
from os import error
filename = 'name.json'
filepath = 'pyy/json/'+filename
with open(filepath)as fp:
    try:
        username = json.load(fp)
        # print("ok"+username)
    except json.decoder.JSONDecodeError:
        username = input("what's your name ?    ")
        with open(filepath, 'w')as fp:
            json.dump(username, fp)
            print("ok")
    else:
        print('welcome '+username)
