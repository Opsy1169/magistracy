import numpy as np


def zern_1_0_0(r, phi):
    return 1


def zern_2_1_minus1(r, phi):
    return 2 * r * np.sin(phi)


def zern_3_1_1(r, phi):
    return 2 * r * np.cos(phi)


def zern_4_2_minus2(r, phi):
    return np.sqrt(6) * r ** 2 * np.sin(2 * phi)


def zern_5_2_0(r, phi):
    return np.sqrt(2) * (2 * r ** 2 - 1)


def zern_6_2_2(r, phi):
    return np.sqrt(6) * r ** 2 * np.cos(2 * phi)


def zern_7_3_minus3(r, phi):
    return 2 * np.sqrt(2) * r ** 3 * np.sin(3 * phi)


def zern_8_3_minus1(r, phi):
    return 2 * np.sqrt(2) * (3 * r ** 3 - 2 * r) * np.sin(phi)


def zern_9_3_1(r, phi):
    return 2 * np.sqrt(2) * (3 * r ** 3 - 2 * r) * np.cos(phi)


def zern_10_3_3(r, phi):
    return 2 * np.sqrt(2) * r ** 3 * np.cos(3 * phi)


def zern_11_4_minus4(r, phi):
    return np.sqrt(10) * r ** 4 * np.sin(4 * phi)


def zern_12_4_minus2(r, phi):
    return np.sqrt(10) * (4 * r ** 4 - 3 * r ** 2) * np.sin(2 * phi)


def zern_13_4_0(r, phi):
    return np.sqrt(5) * (6 * r ** 4 - 6 * r ** 2 + 1)


def zern_14_4_2(r, phi):
    return np.sqrt(10) * (4 * r ** 4 - 3 * r ** 2) * np.cos(2 * phi)


def zern_15_4_4(r, phi):
    return np.sqrt(10) * r ** 4 * np.cos(4 * phi)
