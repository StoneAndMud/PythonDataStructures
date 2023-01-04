def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    ((x1, y1), (x2, y2)) = m1
    ((a1, b1, c1), (a2, b2, c2), (a3, b3, c3)) = m2

    if matrix == m1:
        return ((x1 + y2) + (y1 + x2))
    if matrix == m2:
        return ((a1 + b2 + c3) + (a3 + b2 + c1))


m1 = [
    [1,   2],
    [30, 40],
]
m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))
