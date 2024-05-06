# CS564
How to use redis_file_upload.py
Just run python3 redis_file_upload.py 192.168.20.21 /home/labuser/hello_world.txt /home/labuser/hello_world.txt

# c2 readme
## installation
create virutalenv:

`sudo apt install -y python3.8-venv && sudo apt-get install -y python3-tk python3-dev && python3 -m venv ./c2_venv && source ./c2_venv/bin/activate`

`pip install -r requirements.txt`

alternative:

instead of using virtual environment, just download everything inside the c2_venv which includes all the packages, libraries and binaries.

For python version, please refer to _pycache_

## running
After activate virutal environment and install the requirements. We can start c2 client and implant.py file:

`python implant.py`

open another terminal:

`python c2.py`

## basic usage
### keylogger over stegano
1. start keylogger: input command 'key' in c2
2. get keylogger results: type 'getkeylogger' in c2

keylogger will record all key typing and save the data into 'file.log' fie. When c2 requires the data, implant will send the data over stegano tunnel.If the traffic is captured, only image data will be leaked.
### sql
Using 'sql {query}' command, the query string will be executed in implant server.
### screenshot
Using 'shot' command, the implant will take a screenshot and send back it to c2. The c2 client will pop up a new window show the caputured image.
### delete file
Using 'delete {filepath}' command, if the filepath file exists, it will be deleted.
