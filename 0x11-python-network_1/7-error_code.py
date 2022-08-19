#!/usr/bin/python3
"""
7. Error code #1
"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    status = res.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(res.text)
