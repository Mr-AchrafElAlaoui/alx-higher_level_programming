#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    functions = dir(hidden_4)

    for function in functions:
        if function[:2] != "__":
            print(function)
