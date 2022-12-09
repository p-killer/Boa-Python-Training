import json
import requests  # pip install requests

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=hyderabad&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73")
report = json.loads(response.text)
print(report)
print(type(report))     #dict

desc=report['weather'][0]['description']
print(desc)

for i in report:
    if i=='coord':
        continue
    print(i,':',report[i])
    print('\n')

#---------------------------------------
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos",verify=False)
todos = json.loads(response.text)
# memory level serialization with JSON
data=json.dumps(todos, indent=2)
print(data)

#Serialization
with open("data_file.json", "w") as write_file:    # dump into file
    json.dump(data, write_file)
#Deserialization
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)  # load() for loading the data from file
    print(data)

print("Done")

'''
'''
# Deserialization
todo = dict()
for item in data['title']['completed']:
    name = item['title']
    status = item['competed']
    print ("{} is {}".format(name,status))
    todo[name] = name

print(todo['name'])
'''
