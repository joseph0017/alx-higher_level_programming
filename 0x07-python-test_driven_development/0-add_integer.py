#!/usr/bin/python3
"""
0-add_integer module
0-add_integer supplies one function, add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """Function that add two integers
    Args:
        a: first integer.
        b: second integer, default 98
    Raises:
        TypeError: if a, b are not int, float
    Returns:
        The sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
