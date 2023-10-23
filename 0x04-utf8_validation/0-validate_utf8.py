#!/usr/bin/python3
"""validUTF8 module"""


def validUTF8(data):
    """Determines if given data set represents a valid
    UTF-8 encoding.

    Args:
        data (list): List of integers.

    Returns:
        Bool: True if data is UTF-8 encoded, else False.
    """
    for num in data:
        if (num >> 8) != 0:
            return False

    return True
