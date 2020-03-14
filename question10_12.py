import json

filename = 'number.json'
try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
except FileNotFoundError:
    fav_num = int(input("What is your favourite number?"))
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
    print("I'll remember this number when you come back!")
else:
    print("I know your favorite number! It's " + str(favorite_number) + ".")