import json

f = open('top_cities.json', 'r')
text = json.loads(f.read())
print(text)