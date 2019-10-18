#!/usr/bin/python3
"""

Send multiple POST request to http://158.69.76.135/level0.php
Project is for learning purposes only and this page was created for that

"""
import requests

# Data gotten from a request made from web page

url = 'http://158.69.76.135/level1.php'
with requests.Session() as session:
    response = session.get(url)
    cookie = session.cookies['HoldTheDoor']
    payload = {
        'id': 904,
        'holdthedoor': 'Submit',
        'key': cookie
    }

    for petition in range(4096):
        response = session.post(url, data=payload)
        payload['key'] = session.cookies['HoldTheDoor']
