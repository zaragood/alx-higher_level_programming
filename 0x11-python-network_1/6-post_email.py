#!/usr/bin/python3
""" Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a 
parameter, and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    obj = {'email': sys.argv[2]}
    
    response = requests.post(url, data=obj)
    print(response.text)
