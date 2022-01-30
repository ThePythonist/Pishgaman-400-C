import json

# Convert from JSON to Python

# data = '{ "name":"John", "age":30, "city":"New York"}'
#
# x = json.loads(data)
#
# print(type(x))
# print(x['city'])

# Convert from Python to JSON

data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

x = json.dumps(data)

print(type(x))
print(x)
