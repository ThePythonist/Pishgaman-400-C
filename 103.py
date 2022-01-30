import json

f1 = open('states.json')

data = json.load(f1)

for state in data['states']:
    del state['area_codes']

f2 = open("new_states.json", 'w')

json.dump(data, f2, indent=3)
print('Done')
