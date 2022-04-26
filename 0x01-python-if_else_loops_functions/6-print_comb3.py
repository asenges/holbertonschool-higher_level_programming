#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 9 + 1):
        if i >= j:
            pass
        elif i * 10 + j == 89:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")


