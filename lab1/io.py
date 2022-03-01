import random


def generate_random_matrix(matrix, column):
    while 1:
        print("Введите желаемый размер матрицы:")
        try:
            rowsCnt = int(input())
            break
        except ValueError:
            print("Значение должно быть целым")
    for i in range(rowsCnt):
        matrix.append([])
        for j in range(rowsCnt):
            matrix[i].append(0)
    for i in range(rowsCnt):
        summary = 0
        for j in range(rowsCnt):
            if i != j:
                matrix[i][j] = random.uniform(-100, 100)
                summary += matrix[i][j]
        matrix[i][i] = random.uniform(summary + 1000, summary + 10000)
    for i in range(0, len(matrix)):
        column.append(random.uniform(-100, 100))


def get_from_file(matrix, column):
    print("Введите путь к файлу:")
    path = input()
    try:
        file = open(path, "r")
        text = file.read()
    except FileNotFoundError:
        print("Нет такого файла")
        return
    text = text.replace(',', '.')
    rows = text.split("\n")
    rowsCnt = int(rows[0])
    for i in range(rowsCnt):
        matrix.append([])
        for j in range(rowsCnt):
            matrix[i].append(0)
    for i in range(1, rowsCnt + 1):
        rows[i] = rows[i].split(' ')
    try:
        for i in range(rowsCnt):
            for j in range(rowsCnt):
                matrix[i][j] = float(rows[i + 1][j])
        for i in range(1, rowsCnt + 1):
            column.append(float(rows[i][rowsCnt]))
    except ValueError:
        print("Ошибка обработки файла")
        return


def get_from_terminal(matrix, column):
    while 1:
        print("Введите желаемый размер матрицы:")
        try:
            rowsCnt = int(input())
            break
        except ValueError:
            print("Значение должно быть целым")
    for i in range(rowsCnt):
        matrix.append([])
        for j in range(rowsCnt):
            matrix[i].append(0)

    for i in range(rowsCnt):
        for j in range(rowsCnt):
            while 1:
                print("Введите a_" + str(i) + "_" + str(j))
                try:
                    matrix[i][j] = float(input())
                    break
                except ValueError:
                    print("Значение должно быть целым или десятичной дробью")
    for i in range(rowsCnt):
        while 1:
            print("Введите b_" + str(i))
            try:
                column.append(float(input()))
                break
            except ValueError:
                print("Значение должно быть целым или десятичной дробью")
