#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
You are not allow to import other packages than requests and sys
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])

    print(r.headers.get("X-Request-Id"))
