import json

f = open('states.json')

data = json.load(f)
# print(type(data))
# print(data)

for state in data['states']:
    if int(state['area_codes'][0][-1]) % 2 == 0 :
        print(state['name'], state['area_codes'][0])
