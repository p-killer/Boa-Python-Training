# HTTP Web Services
'''
What is Http Web service?

Exchanging data with remote servers using http is web service.

Explose web service/REST services with DJango framework
or Spring REST  or Web API or Node REST

 To get data from the server, use http GET. 
 To send new data to the server, use http POST.
 To Put,Delete , use http PUT and http DELETE

 Python 3 comes with two different libraries for interacting with
  http web services:

1. http.client  with http protocol.
2. urllib.request  which is an abstraction layer built on top of http.client.

 
pip install httplib2
'''
import httplib2
h = httplib2.Http('.cache') 
#response, content= h.request('http://myfeed.org/examples/feed.xml')
#response, content = h.request('http://www.adp.com')

# invoice third party REST service - openweathermap.org/weather
response,content=h.request('http://api.openweathermap.org/data/2.5/weather?q=chennai&units=imperial&appid=ca3f6d6ca3973a518834983d0b318f73')

print(response.status)
print(content[:100])

desc=content.get('weather')[0].get('description')
print(desc)  # scattered clouds


'''
Posting data to server
------------------------
from urllib.parse import urlencode
import httplib2
h = httplib2.Http('.cache')
data = {'status': 'Test update from Python 3'}
h.add_credentials('murthy', 'MY_SECRET_PASSWORD', 'identi.ca')    ①
resp, content = h.request('https://identi.ca/api/statuses/update.xml',
...     'POST',                                                             ②
...     urlencode(data),                                                    ③
...     headers={'Content-Type': 'application/x-www-form-urlencoded'})      ④

'''
