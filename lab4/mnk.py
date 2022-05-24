from copy import copy
import IO
import exponential
import linear
import quadratic


def get_approximated_points(points, approximation_func):
    approximated_points = []
    deviations = []
    for point in points:
        y1 = approximation_func(point[0])
        approximated_points.append((point[0], y1))
        deviations.append((y1 - point[1]) ** 2)
    return approximated_points, deviations


def calculate_deviation(deviations):
    sum = 0
    for dev in deviations:
        sum += dev
    return sum


def run(points):
    approximation = linear.get_linear
    approximation_func_1 = approximation(points)
    approximated_points_1, deviations_1 = get_approximated_points(points, approximation_func_1)
    deviation_1 = calculate_deviation(deviations_1)
    approximation = quadratic.get_quadratic
    approximation_func_2 = approximation(points)
    approximated_points_2, deviations_2 = get_approximated_points(points, approximation_func_2)
    deviation_2 = calculate_deviation(deviations_2)
    try:
        approximation = exponential.get_exponential
        approximation_func_3 = approximation(points)
        approximated_points_3, deviations_3 = get_approximated_points(points, approximation_func_3)
        deviation_3 = calculate_deviation(deviations_3)
    except ValueError:
        deviation_3 = 999999999
    min_deviation = min(deviation_1, deviation_2, deviation_3)
    if min_deviation == deviation_1:
        return approximation_func_1
    if min_deviation == deviation_2:
        return approximation_func_2
    if min_deviation == deviation_3:
        return approximation_func_3
