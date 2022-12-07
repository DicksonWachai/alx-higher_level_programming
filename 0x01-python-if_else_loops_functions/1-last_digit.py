#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    LastDigit = number % -10
else:
    LastDigit = number % 10
if LastDigit > 5:
    print(f"Last Digit of {number:d} is {LastDigit:d} and is greater than 5")
elif LastDigit == 0:
    print(f"Last Digit of {number:d} is {LastDigit:d} and is 0")
elif LastDigit < 6 and LastDigit != 0:
    print(f"Last Digit of {number:d} is {LastDigit:d} and is less than 6 not 0")
