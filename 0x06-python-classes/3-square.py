#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Square class with a private instance attribute size."""
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Attributes:
            __size (int): The private instance attribute
                representing the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Methode that compute the current square area.

        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size
