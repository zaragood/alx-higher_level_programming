#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    obj = {'email': sys.argv[2]}
    
    response = requests.post(url, data=obj)
    print(response.text)
