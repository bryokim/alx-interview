#!/usr/bin/python3
"""Implementation of canUnlockAll"""


def canUnlockAll(boxes):
    """Determines whether all boxes can be opened.

    Args:
        boxes (list): A list of lists. Each list is a box
            containing keys that open corresponding boxes at
            that index.

    Returns:
        Bool: True if all boxes can be unlocked, False if otherwise
    """

    unlocked = {0}  # The first box is unlocked
    stack = {0}  # Keep track of which box to open next
    size = len(boxes)

    if size == 1:
        return True

    for _ in range(size - 1):
        if len(stack) > 0:
            valid_keys = {
                key
                for key in boxes[stack.pop()]
                if key not in unlocked and key < size
            }

            # Update stack and unlocked.
            stack.update(valid_keys)
            unlocked.update(valid_keys)

            if len(unlocked) == size:  # All boxes are unlocked.
                return True
        else:
            return False

    return False
