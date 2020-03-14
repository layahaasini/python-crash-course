import json

fav_num = int(input("What is your favorite number?"))

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(fav_num, f_obj)