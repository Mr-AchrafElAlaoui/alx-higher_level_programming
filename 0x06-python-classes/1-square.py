#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Square classe with a instance attrubite size. """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The private instance attribute representing
                the size of the square.
        """
        self.__size = size
