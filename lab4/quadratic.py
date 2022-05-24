import numpy as np

import IO


def calculate_coefs(points):
    SX = 0
    SXX = 0
    SXXX = 0
    SX_4 = 0
    SY = 0
    SXY = 0
    SXXY = 0
    for point in points:
        SX += point[0]
        SXX += point[0] ** 2
        SXXX += point[0] ** 3
        SX_4 += point[0] ** 4
        SY += point[1]
        SXY += point[0] * point[1]
        SXXY += (point[0] ** 2) * point[1]

    M = np.array([[len(points), SX, SXX],
                  [SX, SXX, SXXX],
                  [SXX, SXXX, SX_4]])
    V = np.array([SY, SXY, SXXY])

    return np.linalg.solve(M, V)


def get_quadratic(points):
    coefs = calculate_coefs(points)
    return lambda x: coefs[2] * (x ** 2) + coefs[1] * x + coefs[0]
