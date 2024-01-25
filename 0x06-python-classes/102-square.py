#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """A class that defines a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        area(): Calculates the area of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    def __eq__(self, value):
        if isinstance(value, Square):
            return self.area() == value.area()
        return False

    def __ne__(self, value):
        return not self.__eq__(value)

    def __lt__(self, value):
        if isinstance(value, Square):
            return self.area() < value.area()
        return False

    def __le__(self, value):
        if isinstance(value, Square):
            return self.area() <= value.area()
        return False

    def __gt__(self, value):
        if isinstance(value, Square):
            return self.area() > value.area()
        return False

    def __ge__(self, value):
        if isinstance(value, Square):
            return self.area() >= value.area()
        return False

    @property
    def size(self):
        """int: The size of the square.

        The size value must be a integer and >= 0.

        Raises:
            TypeError: Size must be an integer.
            ValueError: Size must be >= 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that compute the current square area.

        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size
