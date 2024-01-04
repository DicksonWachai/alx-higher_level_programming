#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    total = 0
    for i in range(argc):
        total += int(argv[i + 1])
    print(total)
