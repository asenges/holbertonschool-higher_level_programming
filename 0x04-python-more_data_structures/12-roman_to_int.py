#!/usr/bin/python3

def roman_to_int(roman_string):

    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if roman_string is None:
        return 0
    elif type(roman_string) != str:
        return 0
    elif len(roman_string) == 1:
        return roman[roman_string]
    else:
        dec_sum = 0
        dec_numbers = list()
        for i in roman_string:
            dec_numbers.append(roman[i])
        for i in range(1, len(roman_string)):
            if dec_numbers[i - 1] < dec_numbers[i]:
                dec_numbers[i - 1] = -(dec_numbers[i - 1])
        for i in dec_numbers:
            dec_sum += i
        return dec_sum
