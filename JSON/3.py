import json

f = open('states.json')

data = json.load(f)
# print(type(data))
# print(data)

for state in data['states']:
    print(state['name'])
