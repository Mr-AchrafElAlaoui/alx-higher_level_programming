#!/usr/bin/python3

def roman_to_int(roman_string):
    """Function that converts a Roman numeral to an integer"""
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                      "D": 500, "M": 1000, }
    number = 0

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        prev_value = 0
        for roman_char in reversed(roman_string):
            if roman_char in roman_numerals:
                roman_int = roman_numerals.get(roman_char)
                if roman_int < prev_value:
                    number -= roman_int
                else:
                    number += roman_int
                prev_value = roman_int
            else:
                return 0
        return number
