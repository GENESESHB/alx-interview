#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ a function that that returns a list of lists of
        integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    hb = [[1]]

    for i in range(n - 1):
        tempo = [0] + hb[-1] + [0]
        rows = []
        for j in range(len(hb[-1]) + 1):
            rows.append(tempo[j] + tempo[j + 1])
        hb.append(rows)
    return hb
