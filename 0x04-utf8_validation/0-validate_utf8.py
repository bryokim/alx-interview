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
    num_bytes = 0

    for num in data:
        if (num >> 8) != 0:
            return False

        if num_bytes == 0:
            num_bytes = check_num_bytes_in_character(num)

            if num_bytes == 1 and num >> 7 != 0:
                return False

        else:
            # Ensure the leading bytes are 10
            if (num & 0b10000000) or (num | 0b10111111) != 0b10111111:
                return False

        num_bytes -= 1

    if num_bytes > 0:
        # Last character was not encoded correctly.
        return False

    return True


def check_num_bytes_in_character(first_byte):
    """Check the number of bytes in the current character
    encoding.

    Args:
        first_byte (Any): First byte of the character.

    Returns:
        int: Number of bytes in the character encoding.
    """

    x = first_byte & 0b11110000  # first_byte | 240

    if x == 0b11000000 and (first_byte | 0b11011111) == 0b11011111:
        return 2
    elif x == 0b11100000 and (first_byte | 0b11101111) == 0b11101111:
        return 3
    elif x == 0b11110000 and (first_byte | 0b11110111) == 0b11110111:
        return 4
    else:
        return 1
