import json

f = open('states.json')

data = json.load(f)

for state in data['states']:
    print(state['name'], ':', state['area_codes'])
