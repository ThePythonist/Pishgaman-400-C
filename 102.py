import json

f = open('states.json')

data = json.load(f)

# for state in data['states']:
#     print(state['name'],state['area_codes'][0])

for state in data['states']:
    if int(state['area_codes'][0]) % 2 == 0 :
        print(state['name'])
