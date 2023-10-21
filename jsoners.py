import json

to_write = {
    'name': 'Juan',
    'age': 2
}

with open('something.json', 'w') as file:
    json.dump(to_write, file, indent=4)

with open('something.json', 'r') as file:
    data = json.load(file)
    print(data['name'])

