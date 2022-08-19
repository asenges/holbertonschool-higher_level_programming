#!/usr/bin/python3
""""
6. POST an email #1
"""
import requests
from sys import argv


if __name__ == "__main__":
    json = {'email': argv[2]}
    res = requests.post(argv[1], data=json)
    print(res.text)
