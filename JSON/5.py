import json

f = open('states.json')

data = json.load(f)
# print(type(data))
# print(data)

for state in data['states']:
    del state['area_codes']

f2 = open('new_states.json','w')
json.dump(data, f2, indent=2)
print('Done')
