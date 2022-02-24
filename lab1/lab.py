from lab1.method import calc
from lab1.io import get_from_file

def start():
    matrix = []
    column = []
    accuracy = 0
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
                break
            case "2":
                get_from_file(matrix, column, accuracy)
                calc(matrix, column, accuracy)
                break
            case "3":
                print("Рандом - крута!")
                break
            case "/q":
                break
            case _:
                print("Вы ввели некорректное значение")
