#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

len_arguments = len(argv) - 1

if len_arguments > 3 or len_arguments < 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))

    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))

    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))

    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
