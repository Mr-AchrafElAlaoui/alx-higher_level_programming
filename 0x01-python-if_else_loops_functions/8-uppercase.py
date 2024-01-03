#!/usr/bin/python3

def uppercase(str):
    """Print the string in uppercase"""
    for character in str:
        upper_character = character
        if ord(character) in range(97, 123):
            upper_character =chr(ord(character) - 32)
        print("{}".format(upper_character), end="")
    print()
