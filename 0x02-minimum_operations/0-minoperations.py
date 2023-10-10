#!/usr/bin/python3
"""minOperations module"""

import math
from typing import Any


def minOperations(n: Any) -> int:
    """Calculates the fewest number of operations needed to result
    in exactly `n H` characters in a file. The file starts with a single `H`
    character.

    Only two operations can be executed in this file: `Copy All` and `Paste`.

    Description:
        The min number of operations is equal to the min sum of two multiples
        of `n`. If `n` is prime, then the min number of operations is equal to
        `n`.

    Args:
        n (Any): Number of `H` characters expected.

    Returns:
        int: Minimum number of operations to execute.
    """
    if (
        (type(n) is not int and type(n) is not float) or
        n == 0 or
        math.isinf(n)
    ):
        return 0

    if type(n) is float:
        n = math.floor(n)

    mid = math.floor(n / 2)
    min_operations = n

    # Loop until the midpoint.
    for i in range(1, mid + 1):
        if math.fmod(n, i) == 0:
            cur_operations = i + n / i

            if cur_operations < min_operations:
                min_operations = int(cur_operations)

    return min_operations


if __name__ == "__main__":
    print(minOperations(5.5))
