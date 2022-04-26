#!/usr/bin/python3
def pow(a, b):
    power = 1
    if b > 0 and a > 0:
        for i in range (b):
            power *= a
        return power
    elif b > 0 and a < 0:
        for i in range (b):
            power *= abs(a)
        return power
    elif b < 0:
        for i in range (abs(b)):
            power *= a
        return 1 / power    
    else:
        return 1
