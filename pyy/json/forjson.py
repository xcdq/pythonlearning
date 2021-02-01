import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'number.json'
filepath = 'pyy/json/'+filename
with open(filepath, 'w')as f_obj:
    json.dump(numbers, f_obj)
