#!/usr/bin/python3
"""
9. My GitHub!
"""
import requests
from sys import argv

if __name__ == "__main__":
    credentials = (argv[1], argv[2])
    res = requests.get('https://api.github.com/user', auth=credentials)
    print(res.json().get('id'))
