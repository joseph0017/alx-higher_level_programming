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
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))