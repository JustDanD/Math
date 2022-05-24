def get_int():
    try:
        number = int(input(">> "))
        return number
    except EOFError as error:
        print("Экстренное завершение работы")
        SystemExit
    except:
        print("Неправильный ввод, пожалуйста, повторите...")
        return get_int()


def get_int_float():
    try:
        number = float(input(">> "))
        return number
    except EOFError:
        print("Экстренное завершение работы(")
        SystemExit
    except:
        print("Неправильный ввод, пожалуйста, повторите...")
        return get_int_float()


def get_interval():
    print("Введите левую границу: ")
    a = get_int_float()
    print("Введите правую границу: ")
    b = get_int_float()
    return a, b


def get_sigma():
    print("Введите точность :")
    return get_int_float()
