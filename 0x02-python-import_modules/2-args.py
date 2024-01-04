#!/usr/bin/python3
from sys import argv

arguments = len(argv) - 1

if arguments == 0:
    print("{} arguments.".format(arguments))
else:
    print("{} {}".format(arguments, 'argument' if arguments == 1 
          else 'arguments'))
    for index in range(1, arguments + 1):
        print("{}: {}".format(index, argv[index]))
