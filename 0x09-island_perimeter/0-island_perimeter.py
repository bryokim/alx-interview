#!/usr/bin/python3
"""island_perimeter module"""


def count_sides(grid, start, shape, path):
    """Find the total sides of cells with 1 and the
    touching sides of consecutive 1s.

    Args:
        grid (list[list[int]]): A list of list of integers.
        start (list[int, int]): A list of two integers representing
            the starting coordinate.
        shape (tuple[int, int]): A tuple of two integers representing
            the number of rows and columns of the grid.
        path (list[tuple[int, int]]): A list of tuples of coordinates
            already visited .

    Returns:
        tuple[int, int]: A tuple of the total number of sides and the number
            of touching sides.
    """
    touching_sides = 0
    total_sides = 4

    path.append((start[0], start[1]))

    if start[1] + 1 < shape[1] and grid[start[0]][start[1] + 1] == 1:
        touching_sides += 1
        if (start[0], start[1] + 1) not in path:
            x, y = count_sides(grid, (start[0], start[1] + 1), shape, path)
            touching_sides += y
            total_sides += x

    if start[1] - 1 >= 0 and grid[start[0]][start[1] - 1] == 1:
        touching_sides += 1
        if (start[0], start[1] - 1) not in path:
            x, y = count_sides(grid, (start[0], start[1] - 1), shape, path)
            touching_sides += y
            total_sides += x

    if start[0] + 1 < shape[0] and grid[start[0] + 1][start[1]] == 1:
        touching_sides += 1
        if (start[0] + 1, start[1]) not in path:
            x, y = count_sides(grid, (start[0] + 1, start[1]), shape, path)
            touching_sides += y
            total_sides += x

    if start[0] - 1 >= 0 and grid[start[0] - 1][start[1]] == 1:
        touching_sides += 1
        if (start[0] - 1, start[1]) not in path:
            x, y = count_sides(grid, (start[0] - 1, start[1]), shape, path)
            touching_sides += y
            total_sides += x

    return total_sides, touching_sides


def find_first_one(grid):
    """Find the first cell with a 1.

    Args:
        grid (list[list[int]]): A list of list of integers.

    Returns:
        tuple: Tuple of x, y coordinates of the cell. Else -1, -1
            if no cell with 1 is found.
    """
    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                return row, column

    return -1, -1


def island_perimeter(grid):
    """Find the perimeter of an island.

    Each cell is square, with a side length of 1.
    Cells are connected horizontally/vertically (not diagonally).
    `grid` is rectangular, with its width and height not exceeding 100.

    Args:
        grid (list[list[int]]): A list of list of integers.
            0 reps water
            1 reps land

    Returns:
        int: Perimeter.
    """
    row, column = find_first_one(grid)

    if row == -1:
        return 0

    total, touching = count_sides(
        grid[::], [row, column], (len(grid), len(grid[0])), []
    )

    return total - touching
