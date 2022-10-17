# Import the json module:
import json

# Convert from JSON to Python:

# some JSON:
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])