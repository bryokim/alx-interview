#!/usr/bin/python3
"""isWinner module"""


def isWinner(x, nums):
    """Find the winner of a game.

    Description:
        There are two players in the game, Maria and Ben.
        Given a set of consecutive integers starting from `1` up to
        and including `n`, they take turns choosing a prime number
        from the set and removing that number and its multiples from
        the set. The player that cannot make a move loses the game.

        Maria is assumed to start every round and they both play
        optimally.

    Args:
        x (int): Number of rounds.
        nums (list[int]): An array of `n`.

    Returns:
        string | None: Name of the winner or None if there is no winner.
    """
    MARIA = 0
    BEN = 0

    for i in range(x):
        TURN = 0  # 0 for MARIA, 1 for BEN

        numbers = [j for j in range(1, nums[i] + 1)]

        if len(numbers) == 0:
            pass
        elif len(numbers) == 1:
            # A list of 1 only.
            # 1 is not a prime number.
            BEN += 1
        else:
            while len(numbers) > 1:
                # Second number is prime.
                prime_number = numbers[1]

                # Filter the prime number and all its multiples.
                numbers = list(
                    filter(lambda x: x % prime_number != 0, numbers)
                )

                # Switch the turn to the other player.
                TURN = 1 if TURN == 0 else 0

            # Player wins if the losing round was not theirs.
            if TURN == 1:
                MARIA += 1
            else:
                BEN += 1

    if BEN > MARIA:
        winner = "Ben"
    elif MARIA > BEN:
        winner = "Maria"
    else:
        winner = None

    return winner
