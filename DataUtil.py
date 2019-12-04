import cmath

import numpy as np


def make_data_circle(data):
    radius = np.floor(len(data) / 2)
    mid_index = np.ceil(len(data) / 2)
    for i in range(len(data)):
        for j in range(len(data[0])):
            x = abs(j - mid_index)
            y = abs(i - mid_index)
            elem_distance = np.floor(np.sqrt(x ** 2 + y ** 2))
            if elem_distance > radius:
                data[i][j] = 0
    return data


def get_zernike_data(func, left_border, right_border, points_count):
    x = np.linspace(left_border, right_border, points_count)
    y = np.linspace(left_border, right_border, points_count)
    z = []
    zfft = []
    just_zernike = []

    for i in range(len(y)):
        arr = []
        arr_without_exp = []
        for j in range(len(x)):
            (r, phi) = cmath.polar(complex(x[j], y[i]))
            arr_without_exp.append(func(r, phi))
        just_zernike.append(arr_without_exp)
    return just_zernike


def make_exponential(zern_values):
    exponential = []
    for line in zern_values:
        exponential.append(list(map(lambda x: np.exp(1j * x), line)))
    return np.array(exponential)


def make_data_abs(values):
    abs_data = []
    for line in values:
        abs_data.append(list(map(np.abs, line)))
    return np.array(abs_data)


def perform_fft(data):
    data = make_exponential(data)
    data = np.fft.fft2(data)
    data = np.fft.fftshift(data, (0, 1))
    data = make_data_abs(data)
    return data
