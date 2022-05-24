import matplotlib.pyplot as plt
import numpy as np


def draw(points, y, approximation_func_1):
    x = np.linspace(min([i[0] for i in points]), max([i[0] for i in points]), 100)
    fig = plt.figure()

    draw_points(points, "red")
    draw_function(x, approximation_func_1, "green", "-", "точки")
    draw_function(x, y, "blue", ":", "решение")

    plt.grid(True)
    plt.legend(loc='best')
    plt.show()


def draw_points(points, color):
    for point in points:
        plt.scatter(point[0], point[1], color=color)


def draw_function(x, y, color, line_style="-", label="Исходная ф-я"):
    x1 = np.arange(x[0], x[-1], 0.0001)
    plt.plot(x1, [y(i) for i in x1], color=color, linestyle=line_style, label=label)