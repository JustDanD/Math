import math
import IO
import graphic
import numpy as np

import method
import mnk
import linear
import exponential
import quadratic


def generate_points(range, func):
    points = []
    for i in range:
        points.append((i, func(i)))
    return points


if __name__ == '__main__':
    eq = IO.get_eq()
    h = IO.get_h()
    eps = IO.get_eps()
    points = method.myln(eq["diff_eq"], eq["a"], eq["b"], eq["a_y"], h, eps)
    approximated_points_1 = mnk.run(points)
    graphic.draw(points, eq['control'], approximated_points_1)
