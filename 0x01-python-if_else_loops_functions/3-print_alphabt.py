#!/usr/bin/python3
for char in range(ord("a"), ord("z") + 1):
    if char != 113 and char != 101:
        print(chr(char), end="", sep="")
