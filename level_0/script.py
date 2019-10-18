#!/usr/bin/python3
"""

Send multiple POST request to http://158.69.76.135/level0.php
Project is for learning purposes only and this page was created for that

"""
import requests


payload = {
    'id': 904,
    'holdthedoor': 'Submit'
}
url = 'http://158.69.76.135/level0.php'

for petition in range(1024):
    response = requests.post(url, data=payload)

print(response)
