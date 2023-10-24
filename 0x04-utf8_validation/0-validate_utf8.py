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
        ls_8_bits = num & 0b11111111  # check 8 least significant bits.

        if num_bytes == 0:
            num_bytes = check_num_bytes_in_character(ls_8_bits)

            if num_bytes == 1 and ls_8_bits >> 7 != 0:
                return False

            num_bytes -= 1
        else:
            # Ensure the leading bytes are 10
            if (ls_8_bits & 0b10000000) or (
                ls_8_bits | 0b10111111
            ) != 0b10111111:
                return False

            num_bytes -= 1

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

    if x == 0b11000000:
        return 2
    elif x == 0b11100000:
        return 3
    elif x == 0b11110000:
        return 4
    else:
        return 1
