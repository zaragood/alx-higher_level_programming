# 0x11-python-network_1

## Description

This repository contains Python scripts that demonstrate various aspects of network programming in Python. The scripts cover topics such as fetching internet resources, decoding urllib body responses, making HTTP GET and POST requests, working with JSON resources, and manipulating data from external services.

## Learning Objectives

After completing this project, you should be able to:

- Explain how to fetch internet resources with the Python package urllib.
- Describe the process of decoding urllib body responses.
- Demonstrate the use of the Python package requests for making HTTP requests.
- Understand how to make HTTP GET and POST requests.
- Fetch and manipulate JSON resources from external services.

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- Your code should use `pycodestyle` (version 2.8.*)
- All files must be executable
- The length of your files will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Use `get` to access dictionary values by key
- A documentation is not a simple word; it's a real sentence explaining the purpose of the module, class, or method
- Your code should not be executed when imported (use `if __name__ == "__main__":`)

## Tasks

### 0. What's my status? #0

Write a Python script that fetches [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status).

```bash
./0-hbtn_status.py | cat -e
```

### 1. Response header value #0

Write a Python script that takes a URL, sends a request to the URL, and displays the value of the `X-Request-Id` variable found in the header of the response.

```bash
./1-hbtn_header.py https://alx-intranet.hbtn.io
```

### 2. POST an email #0

Write a Python script that takes a URL and an email, sends a POST request to the URL with the email as a parameter, and displays the body of the response (decoded in utf-8).

```bash
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

### 3. Error code #0

Write a Python script that takes a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8). Handle `urllib.error.HTTPError` exceptions and print the HTTP status code.

```bash
./3-error_code.py http://0.0.0.0:5000
./3-error_code.py http://0.0.0.0:5000/status_401
./3-error_code.py http://0.0.0.0:5000/doesnt_exist
./3-error_code.py http://0.0.0.0:5000/status_500
```

### 4. What's my status? #1

Write a Python script that fetches [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) using the `requests` package.

```bash
./4-hbtn_status.py | cat -e
```

### 5. Response header value #1

Write a Python script that takes a URL, sends a request to the URL, and displays the value of the variable `X-Request-Id` in the response header.

```bash
./5-hbtn_header.py https://alx-intranet.hbtn.io
```

### 6. POST an email #1

Write a Python script that takes a URL and an email address, sends a POST request to the URL with the email as a parameter, and displays the body of the response.

```bash
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

### 7. Error code #1

Write a Python script that takes a URL, sends a request to the URL, and displays the body of the response. If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code.

```bash
./7-error_code.py http://0.0.0.0:5000
./7-error_code.py http://0.0.0.0:5000/status_401
./7-error_code.py http://0.0.0.0:5000/doesnt_exist
./7-error_code.py http://0.0.0.0:5000/status_500
```

### 8. Search API

Write a Python script that takes a letter, sends a POST request to [http://0.0.0.0:5000/search_user](http://0.0.0.0:5000/search_user) with the letter as a parameter, and displays the response.

```bash
./8-json_api.py
./8-json_api.py a
./8-json_api.py 2
./8-json_api.py b
```

### 9. My GitHub!

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.

```bash
./10-my_github.py papamuziko cisfun
./10-my_github.py papamuziko wrong_pwd
```
