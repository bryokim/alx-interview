# 0x07-rotate_2d_matrix

Contains a module that implements a function that rotates a 2D matrix by 90 degrees clockwise.

The function can rotate both `n x n` and `m x n` matrices.

## Usage

Rotating a `n x n` matrix.

```Python
rotate_2d_matrix = __import__("0-rotate_2d_matrix").rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)

# Output
[
    [13, 9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4]
]
```

Rotating a `m x n` matrix.

```Python
rotate_2d_matrix = __import__("0-rotate_2d_matrix").rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)

# Output
[
    [17, 13, 9, 5, 1],
    [18, 14, 10, 6, 2],
    [19, 15, 11, 7, 3],
    [20, 16, 12, 8, 4]
]

    matrix = [[1, 2, 3, 4]]
    rotate_2d_matrix(matrix)
    print(matrix)

# Output
[
    [1],
    [2],
    [3],
    [4]
]

    matrix = [[1], [2], [3], [4]]
    rotate_2d_matrix(matrix)
    print(matrix)

# Output
[[4, 3, 2, 1]]
```
