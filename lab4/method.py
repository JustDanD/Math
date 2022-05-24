def runge_kutta(f, a, b, y_a, h, main_method=False):
    if (main_method):
        n = int((b-a)/h)
        if (n < 3):
            n = 3
        h = (b-a)/n
    else:
        n = 3
    points = [(a, y_a)]
    x0 = a
    y0 = y_a
    for i in range(n):
        k0 = h*f(x0, y0)
        k1 = h*f(x0+h/2, y0+k0/2)
        k2 = h*f(x0+h/2, y0+k1/2)
        k3 = h*f(x0+h, y0+k2)
        x0 = x0 + h
        y0 = y0 + (k0 + 2*k1 + 2*k2 + k3)/6
        points.append((x0, y0))

    return points

def myln(f, a, b, y_a, h, eps):
    n = int((b-a)/h)
    if (n < 3):
        n = 3
    h = (b-a)/n

    points = runge_kutta(f, a, b, y_a, h) # (x, y)
    derivs = [f(i[0], i[1]) for i in points] # y' = f(x, y)
    n -= 3
    x0 = points[-1][0]

    for i in range(n):

        # прогноз
        y0 = points[-4][1] + 4/3 * h * (2* derivs[-1] - derivs[-2] + 2*derivs[-3])
        x0 = x0 + h

        #коррекция
        while (True):
            deriv = f(x0, y0)
            y1 = points[-2][1] + h* (deriv + 4 * derivs[-1] + derivs[-2]) / 3
            if abs(y1 - y0) < eps:
                y0 = y1
                deriv = f(x0, y0)
                derivs.append(deriv)
                break
            y0 = y1
        points.append((x0, y0))
    return points