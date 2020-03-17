import json

filename = 'numbers.json'
with open(filename) as f_obj:
    favorite_number = json.load(f_obj)
print("I know your favorite number! It's " + str(favorite_number) + ".")