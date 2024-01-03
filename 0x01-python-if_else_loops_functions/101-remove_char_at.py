#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ""

    for char_index in range(len(str)):

        if char_index == n:
            continue

        new_str = new_str + str[char_index]

    return new_str
