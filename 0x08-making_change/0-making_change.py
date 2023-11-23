#!/usr/bin/python3
"""makeChange module"""

import math


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet
    a given amount total

    Args:
        coins (list): List of available coin values.
        total (int): The amount required.

    Returns:
        int: Fewest number of coins, else 0 if total is 0,
            or -1 if the total given cannot by any number of coins.
    """
    if total <= 0:
        return 0

    if len(coins) == 0:
        return -1

    # Sort the coins in descending order.
    coins.sort(reverse=True)

    current = total
    num_of_coins = 0
    index = 0

    while current > 0:
        x, y = divmod(current, coins[index])

        gcd = math.gcd(*coins[index + 1:])

        if gcd > 0:
            # Reduce quotient until remainder is divisible by other
            # coins remaining. Prevents having coins of higher value
            # adding to the total amount leaving a remainder that isn't
            # divisible with other lower value coins leading to incorrect
            # coin count.
            while math.fmod(y, gcd) > 0 and x > 0:
                x -= 1
                y = current - coins[index] * x

        try:
            x_1, y_1 = divmod(current, coins[index + 1])

            if y_1 == 0 and x_1 == x + 1:
                x = x_1
                y = y_1
        except IndexError:
            pass

        num_of_coins += x
        current = y

        index += 1

        if index == len(coins):
            break

    if current != 0:
        return -1

    return num_of_coins
