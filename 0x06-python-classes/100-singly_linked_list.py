#!/usr/bin/python3

"""This module define node class."""


class Node:
    """Defines a node of a singly linked list.

    Attributes:
        __data (int): The data of the node.
        __next_node (Node): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initializes the Node with data and next_node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the list.
                Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is
                not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        Args:
            value (int): The data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the list.

        Args:
            value (Node): The next node in the list.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list.

    Attributes:
        __head (Node): The head node of the list.
    """

    def __init__(self):
        """Initializes the SinglyLinkedList with a head node set to None."""
        self.__head = None

    def __str__(self):
        """Returns a string representation of the list with
        one node number per line."""
        nodes = []
        node = self.__head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in
        the list (increasing order).

        Args:
            value (int): The data of the new Node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
