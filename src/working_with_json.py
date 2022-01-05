# JSON Dump

import json

car = {
    "name": "911",
    "id": "4711",
    "color": "yellow",
    "features": ["Radio", "6 Gang"]
}

# dumps
text = json.dumps(car)
print(text)

# to file
with open("data.json", "w") as write_file:
    json.dump(car, write_file)
    
# open

with open("data.json", "r") as read_file:
    text = json.load(read_file)
print(f'>>>>> file content: {text}')


# load
text = json.dumps(car)
dic = json.loads(text)
print(f">>>>>> load, name: {dic['name']}")
