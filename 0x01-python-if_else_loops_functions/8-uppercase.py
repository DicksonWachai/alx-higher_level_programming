#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) >= ord('a') and ord(n) <= ord('z'):
            n = chr(ord(n) - 32)
        print("{}".format(n), end="")
    print()
