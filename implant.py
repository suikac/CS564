#!/usr/bin/env python3
import socket

s = socket.socket()
host = socket.gethostname()  # Get local machine name
port = 12345  # Specify the port to connect to

s.connect(("128.119.243.175", port)) # get from ip addr from edlab
import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=server_name;"
                      "Database=db_name;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()

for row in cursor:
    print('row = %r' % (row,))

while True:
    data = s.recv(1024).decode()
    command, text = data.split(" ")
    if command == "sql":
        cursor.execute(text)
        for row in cursor:
            s.send(row.encode('utf-8'))
        cnxn.commit()
    if command == "delete":
        # delete the file and quit
        break
s.close()  # Close the socket when done
