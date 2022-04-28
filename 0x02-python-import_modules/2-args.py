#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    if len(argv) > 1:
        print("{:d} {}".format(len(argv) - 1, 
              "argument:" if len(argv) == 2 else "arguments:"))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
