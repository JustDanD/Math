from numpy import arange
import math
import IO


def get_data(func=None, d_func=None):
    print("Выберите уравнение:\n"
          "(1): sin(x)\n"
          "(2): x^3\n"
          "(3): sin(x) / x\n"
          "(4): 1 / x\n")
    match input():
        case "1":
            func = lambda x: math.sin(x)
            d_func = lambda x: math.sin(x)
        case "2":
            func = lambda x: x * x * x
            d_func = lambda x: 0 * x
        case "3":
            func = lambda x: math.sin(x) / x
            d_func = lambda x: x * math.pow(x, -4) * (
                    4 * x * math.cos(x) - 12 * math.sin(x) + 24 * math.sin(x) * math.pow(x, -2) - 24 * math.cos(
                x) * math.pow(x, -1) + math.sin(x) * math.pow(x, 2))
        case "4":
            func = lambda x: 1 / x
            d_func = lambda x: 24 * math.pow(x, -5)
        case _:
            print("Вы ввели некорректное значение")
            return get_data()
    a, b = IO.get_interval()
    return func, a, b, IO.get_sigma(), d_func


def get_r(a, b, n, d_func, h):
    r = 0
    for i in arange(a, b, h):
        try:
            cur_r = d_func(i)
            cur_r *= math.pow((b - a), 5)
            cur_r /= (180 * math.pow(n, 4))
        except ValueError:
            cur_r = 0
        if abs(cur_r) > r:
            r = abs(cur_r)
    return r


def print_gap(x):
    print("Был найден разрыв функции в точке: " + str(x) + "\nВыполняется расчёт левой и правой от разрыва частей интеграла")


def simpson(func, a, b, eps, d_func):
    integral = 0
    n = int((b - a) / eps)
    h = (b - a) / n

    try:
        integral += func(a)
    except ZeroDivisionError:
        print_gap(a)
    try:
        integral += func(b)
    except ZeroDivisionError:
        print_gap(b)

    for i in range(1, n):
        k = 2 + 2 * (i % 2)
        try:
            integral += k * func(a + i * h)
        except ZeroDivisionError:
            print_gap(a + i * h)
    integral *= h / 3

    if get_r(a, b, n, d_func, h) >= abs(integral):
        raise IOError("Был найден разрыв второго рода")
    else:
        return integral


func, a, b, n, d_func = get_data()
print("Подсчитанный интеграл на интервале от " + str(a) + " до " + str(b) + " равен: ")
print(simpson(func, a, b, n, d_func))
