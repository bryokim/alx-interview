"""Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n

    Args:
        n (int): Size of the triangle.

    Returns:
       list: List of list of integers representing Pascal's
            triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        item = [1]
        j = 0
        prev = triangle[i - 1]

        while j < len(prev) - 1:
            item.append(prev[j] + prev[j + 1])
            j += 1

        item.append(1)
        triangle.append(item)

    return triangle
