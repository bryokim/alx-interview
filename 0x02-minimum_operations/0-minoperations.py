#!/usr/bin/python3
"""minOperations module"""

import math


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to result
    in exactly `n H` characters in a file. The file starts with a single `H`
    character.

    Only two operations can be executed in this file: `Copy All` and `Paste`.

    Description:
        The min number of operations is equal to the min sum of two multiples
        of `n`. If `n` is prime, then the min number of operations is equal to
        `n`.

    Args:
        n (int): Number of `H` characters expected.

    Returns:
        int: Minimum number of operations to execute.
    """
    if type(n) is not int or n == 0:
        if type(n) is float:
            f, _ = math.modf(n)  # Get the fractional part.
            if f != 0:  # If fractional part is not 0
                return 0
        else:
            return 0

    if math.isinf(n):
        return 0

    mid = math.floor(n / 2)
    min_operations: int = n

    # Loop until the midpoint.
    for i in range(1, mid + 1):
        if math.fmod(n, i) == 0:
            cur_operations = i + n / i

            if cur_operations < min_operations:
                min_operations = int(cur_operations)

    return min_operations


if __name__ == "__main__":
    print(minOperations(5))
