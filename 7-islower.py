#!/usr/bin/python3

def islower(c):
    """Check the character if it is lower or upper case"""
    if ord(c) in range(97, 123):
        return True
    else:
        return False
