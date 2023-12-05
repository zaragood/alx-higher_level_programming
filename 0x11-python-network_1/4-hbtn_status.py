#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
