'''
Python urllib3

 The Hypertext Transfer Protocol (HTTP) is an application protocol for
  distributed, collaborative, hypermedia information systems. 
  
HTTP is the foundation of data communication for the World Wide Web.


The urllib3 module is a powerful, sanity-friendly HTTP client for Python.

It supports thread safety, connection pooling, client-side SSL/TLS verification,
 file uploads with multipart encoding, helpers for retrying requests and
  dealing with HTTP redirects, gzip and deflate encoding, and proxy for 
  HTTP and SOCKS.

$ pip install urllib3

'''
import urllib3
print(urllib3.__version__)
#-------------------------------------------------

http = urllib3.PoolManager()
url = 'http://webcode.me'
resp = http.request('GET', url)
print(resp.status) # •	Successful responses (200–299)

#-------------------------------------------------
#print data
print(resp.data.decode('utf-8')) # prints content of html file.
#---------------------------------------------------
# getting header information

resp = http.request('HEAD', url)
print(resp.headers['Server'])
print(resp.headers['Date'])
print(resp.headers['Content-Type'])
print(resp.headers['Last-Modified'])
#----------------------------------------------

# certificate    $ pip install certifi
# install certificate now
import certifi
print(certifi.where())
#To reference the installed certificate authority (CA) bundle, 
# we use the built-in where() function.
url = 'https://httpbin.org/anything'
http = urllib3.PoolManager(ca_certs=certifi.where())
resp = http.request('GET', url)
print(resp.status)
#----------------------------------------------------

# urllib3 query parameters:
http = urllib3.PoolManager(ca_certs=certifi.where())
payload = {'name': 'Murthy', 'age': 54}
url = 'https://httpbin.org/get'
req = http.request('GET', url, fields=payload)
print(req.data.decode('utf-8'))
#----------------------------------------------------

#urllib3 post request
http = urllib3.PoolManager(ca_certs=certifi.where())
url = 'https://httpbin.org/post'
req = http.request('POST', url, fields={'name': 'Murthy'})
print(req.data.decode('utf-8'))
'''
Output:
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "name": "Murthy"
  },
  ...
  "url": "https://httpbin.org/post"
}
'''

#urllib3 send JSON
#In requests, such as POST or PUT, the client tells the server what 
# type of data is actually sent with the Content-Type header
import urllib3
import certifi
import json
http = urllib3.PoolManager(ca_certs=certifi.where())

payload = {'name': 'Murthy'}
encoded_data = json.dumps(payload).encode('utf-8')

resp = http.request(
     'POST',
     'https://httpbin.org/post',
     body=encoded_data,
     headers={'Content-Type': 'application/json'})

data = json.loads(resp.data.decode('utf-8'))['json']
print(data)
#----------------------------------------------------------
#urllib3 binary data
import urllib3
http = urllib3.PoolManager()
url = 'http://webcode.me/favicon.ico'
req = http.request('GET', url)
with open('favicon.ico', 'wb') as f:
    f.write(req.data)
#observe favicon.ico file
#---------------------------------------------------------

#urlllib3 with stream of data
import urllib3
import certifi

url = "https://docs.oracle.com/javase/specs/jls/se8/jls8.pdf"

local_filename = url.split('/')[-1]  #jls8.pdf
http = urllib3.PoolManager(ca_certs=certifi.where())

resp = http.request(
    'GET',
    url,
    preload_content=False)

with open(local_filename, 'wb') as f:
    for chunk in resp.stream(1024):
        f.write(chunk)

resp.release_conn()
#In the example, we download a PDF file.


