import math

equations = """
(1) y' = y - x^2 + 2; y(a) = 0; [a,b] = [0, 3]; Решение: y = 0*e^x + x^2 + 2x + 0
(2) y' = y/x; y(a) = 6; [a,b] = [3, 6]; Решение: y = 2x
(3) y' = by; y(a) = 6; [a,b] = [0, 0.8]; Решение: y = 6e^(bx)
"""

def get_b():
    try:
        num = float(input("Введите коэфицент b: ").strip())
        return num
    except Exception:
        get_b()

def get_eq():
    print(equations)
    samp = input("Выберите уравнение: ").strip()
    eq = {}
    match samp:
        case '1':
            eq["diff_eq"] = lambda x, y: y - x**2 + 2
            eq["a"] = 0
            eq["b"] = 3
            eq["a_y"] = 0
            eq["control"] = lambda x: x**2 + 2*x
        case '2':
            eq["diff_eq"] = lambda x, y:  y/x
            eq["a"] = 3
            eq["b"] = 6
            eq["a_y"] = 6
            eq["control"] = lambda x: 2*x
        case '3':
            b = get_b()
            eq["diff_eq"] = lambda x, y: b*y
            eq["a"] = 0
            eq["b"] = 0.8
            eq["a_y"] = 6
            eq["control"] = lambda x: 6*math.exp(b*x)
        case _:
            return get_eq()
    return eq

def get_h():
    try:
        num = float(input("Input h: ").strip())
        return num
    except Exception:
        return get_h()

def get_eps():
    try:
        num = float(input("Input eps: ").strip())
        return num
    except Exception:
        return get_eps()

