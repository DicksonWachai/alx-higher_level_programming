#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if n < 0:
        last_digit = n % -10
        print(-(last_digit), end='')
    else:
        last_digit = n % 10
        print(last_digit, end='')
    return abs(last_digit)
