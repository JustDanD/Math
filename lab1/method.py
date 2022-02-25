def diagonal_dominating(matrix):
    summary = 0
    flag = True

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i != j:
                summary = summary + matrix[i][j]
    print(summary)
    for i in range(0, len(matrix)):
        if matrix[i][i] < summary:
            flag = False
            break
    return flag


def calc(matrix, column, accuracy):
    print(diagonal_dominating(matrix))
