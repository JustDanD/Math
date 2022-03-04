import math
from decimal import Decimal


def diagonal_dominating(matrix):
    flag = True
    count = 0
    for i in range(0, len(matrix)):
        summary = 0
        for j in range(0, len(matrix)):
            if i != j:
                summary = summary + matrix[i][j]
        if matrix[i][i] > summary:
            count += 1
        if matrix[i][i] < summary:
            flag = False
            break
    if count == 0:
        flag = False
    return flag


def gauss_jordan(m, eps):
    (h, w) = (len(m), len(m[0]))
    for i in range(0, h):
        max_row = i
        for j in range(i + 1, h):    # Find max pivot
            if abs(m[j][i]) > abs(m[max_row][i]):
                max_row = j
        (m[i], m[max_row]) = (m[max_row], m[i])
        if abs(m[i][i]) <= eps:     # Singular?
            return False
        for j in range(i + 1, h):    # Eliminate column y
            c = m[j][i] / m[i][i]
            for x in range(i, w):
                m[j][x] -= m[i][x] * c
    for i in range(h-1, 0-1, -1):  # Backsubstitute
        c = m[i][i]
        for j in range(0, i):
            for x in range(w-1, i-1, -1):
                m[j][x] -= m[i][x] * m[j][i] / c
        m[i][i] /= c
        for x in range(h, w):       # Normalize row y
            m[i][x] /= c
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
            res.append(0)
        for i in range(len(column)):
            prev_res.append(0)
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
