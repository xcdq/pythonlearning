import json
filename = 'number.json'
filepath = 'pyy/json/'+filename
with open(filepath)as f_obj:
    numbers = json.load(f_obj)
print(numbers)
