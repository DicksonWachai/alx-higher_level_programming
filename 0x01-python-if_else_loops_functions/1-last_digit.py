#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
start_string = "Last digit of"
if (number < 0):
    last_digit = number % -10
else:
    last_digit = number % 10
if (last_digit == 0):
    print_value = "and is 0"
elif (last_digit > 5):
    print_value = "and is greater than 5"
elif (last_digit < 6 and last_digit != 0):
    print_value = "and is less than 6 and not 0"
print(f"{start_string} {number} is {last_digit} {print_value}")
