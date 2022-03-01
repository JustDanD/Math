from lab1.method import calculate
from lab1.io import *


def execute(matrix, column):
    eps = 0
    digits = 5
    while 1:
        try:
                print("Введите желаемую точность:")
                eps = float(input())
                break
        except ValueError:
            print("Точность должна быть десятичным числом")
    while 1:
        try:
            print("Введите желаемое количество десятичных:")
            digits = int(input())
            break
        except ValueError:
            print("Точность должна быть целым числом")
    res, count, accuracy = calculate(matrix, column, eps)
    if count > 0:
        print("Решения:")
        for i in range(len(column)):
            print(round(res[i], digits))
        print("Погрешности:")
        for i in range(len(column)):
            print(accuracy[i])
        print("Количество итераций:")
        print(count)
    if count == -1:
        print("Не выполняется диагональное преобладание")


def start():
    matrix = []
    column = []
    methods = ["Терминал", "Файл", "Случайно сгенерировать матрицу"]
    i = 1
    while 1:
        print("Укажите, как хотите ввести данные")
        for methodName in methods:
            print(str(i) + ") " + methodName)
            i = i + 1
        match input():
            case "1":
                print("Терминал - крута!")
                get_from_terminal(matrix, column)
                execute(matrix, column)
                break
            case "2":
                get_from_file(matrix, column)
                execute(matrix, column)
                break
            case "3":
                print("Рандом - крута!")
                generate_random_matrix(matrix, column)
                execute(matrix, column)
                break
            case "/q":
                break
            case _:
                print("Вы ввели некорректное значение")
