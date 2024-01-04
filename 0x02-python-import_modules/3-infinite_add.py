#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    arguments = len(argv) - 1
    result = 0

    if arguments == 0:
        result = 0
    else:
        for index in range(1, arguments + 1):
            result += int(argv[index])

    print("{}".format(result))
