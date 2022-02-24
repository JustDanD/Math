import lab1

labs = ["Лабораторная работа 1"]
i = 1


while 1:
    print("Выберите лабораторную работу для запуска (для выхода введите /q ):")
    for labName in labs:
        print(str(i) + ") " + labName)
    match input():
        case "1":
            lab1.lab.start()
        case "/q":
            break
        case _:
            print("Вы ввели некорректное значение")
