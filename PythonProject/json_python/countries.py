import json

json_file = open('/Users/vihrenpironski/Dropbox/Mac/Desktop/workspace/VisualStudioCode/json/countries.json')
data = json.load(json_file)


print(data[0])
print(data[0]['name'])

for country in data:
    if country['name'][0].upper() == 'U':
        print(country)

for country in data:
    if country['code'][1].upper() == 'G':
        print(json.dumps(country, indent=2))

print(json.dumps(data, sort_keys=True, indent=2))

output = open('countries-out.json', 'w')
json.dump(data, output, indent=2)