#!/usr/bin/python3
"""rotate_2d_matrix module"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise.
    The matrix is rotated in place.

    Args:
        matrix (list[list[int]]): A 2D matrix.
    """
    rows = len(matrix)
    columns = len(matrix[0])

    # Index where the matrix ceases to be a square matrix.
    # Helps in maintaining a constant index when looping over
    # elements whose positions are being changed and the old
    # ones deleted. Prevents raising IndexError
    LIMIT = rows if rows < columns else columns

    for i in range(rows):
        for j in range(i, columns):
            try:
                # Swap elements that are in a square matrix.
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            except IndexError:
                # Number of columns exceed rows.
                # Add an extra row at index j in the matrix.

                if i == 0:
                    matrix.append([matrix[i][LIMIT]])
                else:
                    matrix[j].insert(0, matrix[i][LIMIT])

                del matrix[i][LIMIT]

        if i < columns:
            # Reverse rows containing swapped elements.
            matrix[i].reverse()
        else:
            # Number of rows exceed columns.
            # Convert extra rows into columns.
            for j in range(columns):
                matrix[j].insert(0, matrix[LIMIT][j])

            del matrix[LIMIT]
