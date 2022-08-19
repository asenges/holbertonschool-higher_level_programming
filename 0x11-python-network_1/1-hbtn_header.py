#!/usr/bin/python3
""" 
1. Response header value #0
"""
from urllib import request
from sys import argv 

if __name__ == "__main__":
    if argv[1] is not None:
        with request.urlopen(argv[1]) as res:
            print(res.headers.get("X-Request-Id"))
