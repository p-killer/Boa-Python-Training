'''
urllib3 with flask application


In the following example, we send a request to a small Flask web application.

$ pip install flask
'''
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/headers')
def hello():
    ua = request.headers.get('user-agent')
    ka = request.headers.get('connection')

    return f'User agent: {ua}; Connection: {ka}'