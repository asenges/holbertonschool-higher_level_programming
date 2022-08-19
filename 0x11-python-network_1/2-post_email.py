#!/usr/bin/python3
"""
2. POST an email #0
"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    json = parse.urlencode({'email': argv[2]})
    json = json.encode('ascii')
    with request.urlopen(argv[1], json) as res:
        print(res.read().decode('utf-8'))
