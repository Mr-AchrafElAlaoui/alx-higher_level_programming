#!/usr/bin/python3
for first_digit in range(0, 9):
    for last_digit in range(first_digit + 1, 10):
        if first_digit == 8 and last_digit == 9:
            print(f"{first_digit}{last_digit}")
        else:
            print(f"{first_digit}{last_digit}", end=", ")
