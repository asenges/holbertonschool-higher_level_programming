#!/usr/bin/python3
"""
8. Search API
"""
import requests
from sys import argv


if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]
    res = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        json = res.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except ValueError:
        print("Not a valid JSON")
