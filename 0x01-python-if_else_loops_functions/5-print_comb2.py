#!/usr/bin/python3
for char in range(0, 99 + 1):
    if char == 99:
        print(f"{char}")
    else:
        print(f"{char:02}", end=", ")
