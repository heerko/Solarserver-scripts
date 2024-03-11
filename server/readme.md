# Solar Server scripts #

This directory contains script related to getting information related to the webserver to the website over Tinc. 
Create the venv then install the requirments with `pip install -r requirements.txt`.
Goal is to get information about the server to the website. Because we're using tinc for networking and I don't want to open and forward extra ports we're using websockets because it can use the same connection as Ngnix. 

- [`myenv`](myenv) excluded from this repo
- [`gsm.py`](gsm.py)
- [`pijuice_status.py`](pijuice_status.py) 
- [`readme.md`](readme.md) this file
- [`requirements.txt`](requirements.txt) install with `pip install -r requirements.txt`
- [`server.py`](server.py) 
