import numpy as np

import IO


def calculate_coefs(points):
    SX = 0
    SXX = 0
    SY = 0
    SXY = 0
    for point in points:
        SX += point[0]
        SXX += point[0] ** 2
        SY += point[1]
        SXY += point[0] * point[1]
    M = np.array([[SXX, SX], [SX, len(points)]])
    V = np.array([SXY, SY])

    return np.linalg.solve(M, V)


def get_linear(points):
    coefs = calculate_coefs(points)
    return lambda x: coefs[0]*x + coefs[1]