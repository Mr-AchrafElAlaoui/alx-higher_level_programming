#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """A class that defines a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): Atuple representing the position of the square.

    Methods:
        area(): Calculates the area of the square.
        my_print(): Prints the square with '#' character.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): A tuple representing the position
                of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The lenght of the sides of the square.

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
        else:
            self.__size = value

    @property
    def position(self):
        """tuple: The position of the square.

        The position must be a tuple of 2 positive integers.

        Raises:
            TypeError: Position must be a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not len(value) == 2 or
                not all(isinstance(element, int) for element in value) or
                not all(element >= 0 for element in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method that calculates the area of the square.

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """Method that prints the square with '#' character.
        """
        if self.__size == 0:
            print()
        else:
            for new_line in range(self.__position[1]):
                print("")

            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                for _ in range(self.__size):
                    print("#", end="")
                print("")
