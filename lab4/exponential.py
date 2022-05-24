import math
import numpy as np
import IO


def calculate_coefs(points):
    SX = 0
    SXX = 0
    SLnY = 0
    SLnYX = 0
    for point in points:
        SX += point[0]
        SXX += point[0] ** 2
        SLnY += math.log(point[1])
        SLnYX += point[0] * math.log(point[1])
    M = np.array([[len(points), SX], [SX, SXX]])
    V = np.array([SLnY, SLnYX])

    return np.linalg.solve(M, V)


def get_exponential(points):
    coefs = calculate_coefs(points)
    coefs[0] = math.e ** coefs[0]
    return lambda x: coefs[0] * math.e ** (coefs[1]*x)