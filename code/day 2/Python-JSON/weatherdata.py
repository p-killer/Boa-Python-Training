import json
import requests

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=hyderabad&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73")
report = json.loads(response.text)
print(report)

#1. first display the description  of first city which is hyderbad
#2. Display complete weather report for India only (not pakisthan)
# not coords.

coord = report["coord"]
print("Longitude    :", coord["lon"])
print("Latitude     :", coord["lat"])

weather = report["weather"]
print("Weather      :", weather[0]["main"], "-", weather[0]["description"])