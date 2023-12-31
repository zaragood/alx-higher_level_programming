#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
    You must use the package urllib
    You are not allowed to import any packages other than urllib
    The body of the response must be displayed like the following example
    You must use a with statement
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf8')}")
