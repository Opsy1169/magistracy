import numpy as np

from Point import Point


def zern_1_0_0(polar_point: Point):
    return 1


def zern_2_1_minus1(polar_point: Point):
    return 2 * polar_point.x * np.sin(polar_point.y)


def zern_3_1_1(polar_point: Point):
    return 2 * polar_point.x * np.cos(polar_point.y)


def zern_4_2_minus2(polar_point: Point):
    return np.sqrt(6) * polar_point.x ** 2 * np.sin(2 * polar_point.y)


def zern_5_2_0(polar_point: Point):
    return np.sqrt(2) * (2 * polar_point.x ** 2 - 1)


def zern_6_2_2(polar_point: Point):
    return np.sqrt(6) * polar_point.x ** 2 * np.cos(2 * polar_point.y)


def zern_7_3_minus3(polar_point: Point):
    return 2 * np.sqrt(2) * polar_point.x ** 3 * np.sin(3 * polar_point.y)


def zern_8_3_minus1(polar_point: Point):
    return 2 * np.sqrt(2) * (3 * polar_point.x ** 3 - 2 * polar_point.x) * np.sin(polar_point.y)


def zern_9_3_1(polar_point: Point):
    return 2 * np.sqrt(2) * (3 * polar_point.x ** 3 - 2 * polar_point.x) * np.cos(polar_point.y)


def zern_10_3_3(polar_point: Point):
    return 2 * np.sqrt(2) * polar_point.x ** 3 * np.cos(3 * polar_point.y)


def zern_11_4_minus4(polar_point: Point):
    return np.sqrt(10) * polar_point.x ** 4 * np.sin(4 * polar_point.y)


def zern_12_4_minus2(polar_point: Point):
    return np.sqrt(10) * (4 * polar_point.x ** 4 - 3 * polar_point.x ** 2) * np.sin(2 * polar_point.y)


def zern_13_4_0(polar_point: Point):
    return np.sqrt(5) * (6 * polar_point.x ** 4 - 6 * polar_point.x ** 2 + 1)


def zern_14_4_2(polar_point: Point):
    return np.sqrt(10) * (4 * polar_point.x ** 4 - 3 * polar_point.x ** 2) * np.cos(2 * polar_point.y)


def zern_15_4_4(polar_point: Point):
    return np.sqrt(10) * polar_point.x ** 4 * np.cos(4 * polar_point.y)
