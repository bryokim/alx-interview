#!/usr/bin/python3
"""Module for solving the N queens puzzle
The N queens puzzle is the challenge of placing N
non-attacking queens on an NxN chessboard
"""

import sys


def main():
    """Entry point"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    find_queens(n)


def find_queens(n):
    """Find the positions of the non-attacking queens"""

    paths = []
    for index in range(n):
        next_indexes = get_next_indexes(index, n)
        forbidden = gen_forbidden(index, 1, n)
        paths.extend(find_paths(next_indexes, forbidden, 2, n, [index]))

    for path in paths:
        print([[i, path[i]] for i in range(n)])


def find_paths(next, forbidden, index, n, prev_path):
    """Find paths that link non-attacking queens.
    Returned indexes are of the x-axis.
    Top left corner of the board is assumed to be origin (0,0).

    Args:
        next (function): Indexes of possible non-attacking queens.
        forbidden (set): Indexes that queens are attacking.
        index (int): Next index to find it's non-attacking queens.
            This is the index along the y-axis. Top is 0.
        n (int): Number of queens.
        prev_path (list): List of the previous path.

    Returns:
        List[List[int]]: A list of lists of indexes along the x axis
            from left to right that non-attacking queens can be placed.
    """
    if index == n:
        return next

    paths = []
    for i in next:
        path = prev_path[::]
        path.append(i)

        next_1 = get_next_indexes(i, n, forbidden[index])
        if next_1:
            f = gen_forbidden(i, index, n, forbidden)
            r = find_paths(next_1, f, index + 1, n, path)
            if len(r) == 1:
                path.extend(r)
            if type(r) is list and len(r) > 0 and type(r[0]) is list:
                paths.extend(r)
        else:
            path.extend([])

        if len(path) == n:
            paths.append(path)

    return paths


def get_next_indexes(current_index, n, forbidden=None):
    """Get the next indexes on along the x-axis where queens are
    non-attacking.

    Args:
        current_index (int): The current index where a queen has been placed.
        n (int): number of queens. Same as size of chessboard.
        forbidden (set, optional): Set of indexes where the queens
            are attacking in the next row. Defaults to None.

    Returns:
        List: List of indexes where queens are non-attacking.
    """
    x = [j for j in range(current_index - 2, -1, -1)]
    y = [j for j in range(current_index + 2, n)]

    x.reverse()
    x.extend(y)

    to_remove = []
    if forbidden:
        for j in x:
            if j in forbidden:
                to_remove.append(j)

    if to_remove:
        for j in to_remove:
            x.remove(j)

    return x


def gen_forbidden(cur_index, start, n, prev={}):
    """Get indexes where queens are attacking.

    Args:
        cur_index (int): Current index where a queen has been placed.
        start (int): Index along the y-axis from which to check for the
            indexes.
        n (int): Number of queens. Same as size of chessboard.
        prev (dict, optional): Previously calculated forbidden indexes.
            Defaults to {}.

    Returns:
        dict: Forbidden indexes.
    """
    forbidden = {}
    s = 1
    for j in range(start, n):
        x = {-1}

        if cur_index - s >= 0:
            x.update([cur_index - s])

        x.update([cur_index])
        if cur_index + s < n:
            x.update([cur_index + s])

        if prev:
            forbidden[j] = copy_set(prev[j])

        if forbidden.get(j):
            forbidden[j].update(x)
        else:
            forbidden[j] = x

        s += 1

    return forbidden


def copy_set(value):
    """Copy a set given as value"""
    copy = {-1}

    for i in value:
        copy.add(i)

    return copy


if __name__ == "__main__":
    main()
