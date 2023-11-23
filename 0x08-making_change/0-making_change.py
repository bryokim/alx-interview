#!/usr/bin/python3
"""makeChange module"""

import math


def gcd(a, b):
    """Find gcd of 2 integers.

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: gcd
    """
    if a == 0:
        return b
    if b == 0:
        return a

    # base case
    if a == b:
        return a

    # a is greater
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


def gcd_list(*integers):
    """Find gcd of a list of integers

    Returns:
        int: gcd
    """
    if len(integers) == 0:
        return 0

    if len(integers) == 1:
        return integers[0]

    num1 = integers[0]
    num2 = integers[1]

    x = gcd(num1, num2)

    for i in range(2, len(integers)):
        x = gcd(x, integers[i])

    return x


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

    while current > 0 and index < len(coins):
        quotient, remainder = divmod(current, coins[index])

        gcd = gcd_list(*coins[index + 1:])

        if gcd > 0:
            # Reduce quotient until remainder is divisible by other
            # coins remaining. Prevents having coins of higher value
            # adding to the total amount leaving a remainder that isn't
            # divisible with other lower value coins leading to incorrect
            # coin count.
            while math.fmod(remainder, gcd) > 0 and quotient > 0:
                quotient -= 1
                remainder = current - coins[index] * quotient

        try:
            # Check if the next coin value can fully divide the amount
            # with a lesser count.
            x_1, y_1 = divmod(current, coins[index + 1])

            if y_1 == 0 and x_1 == quotient + 1:
                quotient = x_1
                remainder = y_1
        except IndexError:
            pass

        num_of_coins += quotient
        current = remainder

        index += 1

    if current != 0:
        return -1

    return num_of_coins
