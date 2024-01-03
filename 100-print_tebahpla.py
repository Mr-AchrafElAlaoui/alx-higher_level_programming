#!/usr/bin/python3

for ascii_character in range(122, 96, -1):
    character = chr(ascii_character)

    if ascii_character % 2 != 0:
        character = chr(ascii_character - 32)

    print("{}".format(character), end="")
