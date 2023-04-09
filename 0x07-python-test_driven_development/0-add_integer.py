#!/usr/bin/python3

"""
Module to add two integers
"""

def add_integer(a, b = 98) -> int:
    """Returns integer addition of a and b.

    Float arguments are typecasted as integers before addition

    Args:
        a: The first number to be added.
        b: The second number to be added. Defaults to 98.

    Raises:
        TypeError: If either a or b are non-integer or non-float.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or float')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or float')
    return int(a) + int(b)
