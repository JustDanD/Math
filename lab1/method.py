import math
from decimal import Decimal


def diagonal_dominating(matrix):
    flag = True

    for i in range(0, len(matrix)):
        summary = 0
        for j in range(0, len(matrix)):
            if i != j:
                summary = summary + matrix[i][j]
        if matrix[i][i] < summary:
            flag = False
            break
    return flag


def gauss_jordan(m, eps):
    """Puts given matrix (2D array) into the Reduced Row Echelon Form.
       Returns True if successful, False if 'm' is singular.
       NOTE: make sure all the matrix items support fractions! Int matrix will NOT work!
       Written by Jarno Elonen in April 2005, released into Public Domain"""
    (h, w) = (len(m), len(m[0]))
    for y in range(0,h):
        maxrow = y
        for y2 in range(y+1, h):    # Find max pivot
            if abs(m[y2][y]) > abs(m[maxrow][y]):
                maxrow = y2
        (m[y], m[maxrow]) = (m[maxrow], m[y])
        if abs(m[y][y]) <= eps:     # Singular?
            return False
        for y2 in range(y+1, h):    # Eliminate column y
            c = m[y2][y] / m[y][y]
            for x in range(y, w):
                m[y2][x] -= m[y][x] * c
    for y in range(h-1, 0-1, -1): # Backsubstitute
        c  = m[y][y]
        for y2 in range(0,y):
            for x in range(w-1, y-1, -1):
                m[y2][x] -=  m[y][x] * m[y2][y] / c
        m[y][y] /= c
        for x in range(h, w):       # Normalize row y
            m[y][x] /= c
    return True

def converge(xk, xkp, eps):
    flag = True
    for i in range(len(xk)):
        flag = math.sqrt(Decimal((xk[i] - xkp[i]) * (xk[i] - xkp[i]))) < eps
        if not flag:
            break
    return flag


def calculate(matrix, column, eps):
    res = []
    prev_res = []
    accuracy = []
    if diagonal_dominating(matrix):
        for i in range(len(column)):
            res.append(1)
        for i in range(len(column)):
            prev_res.append(1)
        for i in range(len(column)):
            accuracy.append(0)
        count = 0
        while 1:
            for i in range(len(column)):
                prev_res[i] = res[i]
            for i in range(len(column)):
                tmp = 0
                for j in range(len(column)):
                    if j != i:
                        tmp += (matrix[i][j] * prev_res[j])
                res[i] = (column[i] - tmp) / matrix[i][i]
                accuracy[i] = res[i] - prev_res[i]
            count += 1
            if converge(res, prev_res, eps):
                break
    else:
        tmp_mtx = []
        for i in range(len(column)):
            tmp_mtx.append([])
            for j in range(len(column)):
                tmp_mtx[i].append(matrix[i][j])
        for i in range(len(column)):
            tmp_mtx[i].append(column[i])
        gauss_jordan(tmp_mtx, eps)
        for i in range(len(column)):
            for j in range(len(column)):
                matrix[i][j] = tmp_mtx[i][j]
            column[i] = tmp_mtx[i][len(column)]
        return calculate(matrix, column, eps)
    return res, count, accuracy
