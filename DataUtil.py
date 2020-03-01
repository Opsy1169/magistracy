import cmath
import time

from ZernikeFunctions import *

zern_func = [zern_1_0_0, zern_2_1_minus1, zern_3_1_1, zern_4_2_minus2, zern_5_2_0, zern_6_2_2, zern_7_3_minus3,
             zern_8_3_minus1, zern_9_3_1, zern_10_3_3, zern_11_4_minus4, zern_12_4_minus2, zern_13_4_0, zern_14_4_2,
             zern_15_4_4]


def make_data_circle(data):
    tic = time.time()
    radius = np.floor(len(data) / 2)
    mid_index = np.ceil(len(data) / 2)
    for i in range(len(data)):
        for j in range(len(data[0])):
            x = abs(j - mid_index)
            y = abs(i - mid_index)
            elem_distance = np.floor(np.sqrt(x ** 2 + y ** 2))
            if elem_distance > radius:
                data[i][j] = 0
    toc = time.time()
    print("make_data_circle ", toc - tic)
    return data


def build_grid(x, y):
    grid = []
    for i in range(len(y)):
        row = []
        for j in range(len(x)):
            (r, phi) = cmath.polar(complex(x[j], y[i]))
            row.append(Point(r, phi))
        grid.append(row)
    return np.array(grid)


def get_zernike_data(coeffs, left_border, right_border, points_count):
    tic = time.time()
    x = np.linspace(left_border, right_border, points_count)
    y = np.linspace(left_border, right_border, points_count)
    grid = build_grid(x, y)
    just_zernike = []
    # func = np.vectorize(func)
    # for i in range(len(y)):
    #     arr_without_exp = []
    #     for j in range(len(x)):
    #
    #         superposition = 0
    #         for k in range(len(func)):
    #             superposition += func[k]()*coeffs[k]
    #         arr_without_exp.append(superposition)
    #     just_zernike.append(arr_without_exp)
    just_zernike = np.full((points_count, points_count), (0 + 0j))
    for i in range(len(zern_func)):
        tic1 = time.time()
        func_k = np.vectorize(zern_func[i])
        just_zernike += func_k(grid) * coeffs[i]
        toc1 = time.time()
        print("zern ", toc1 - tic1)
    toc = time.time()
    print("get_zernike_data ", toc - tic)
    return just_zernike


def make_exponential(zern_values, coeff=1.0):
    tic = time.time()
    exponential = []
    for line in zern_values:
        exponential.append(list(map(lambda x: np.exp(1j * coeff * x), line)))
    toc = time.time()
    print("make_exponential ", toc - tic)
    return np.array(exponential)


def make_data_abs(values):
    tic = time.time()
    abs_data = np.abs(values)
    toc = time.time()
    print("make_data_abs ", toc - tic)
    return abs_data


def expand_data_with_zeroz(data, times_to_expand_dimension):
    tic = time.time()
    zeros = np.full((data.shape[0] * times_to_expand_dimension, data.shape[1] * times_to_expand_dimension), (0 + 0j))
    zeros[:data.shape[0], :data.shape[1]] = data
    data = zeros
    toc = time.time()
    print("expand_data_with_zeroz ", toc - tic)
    return data


# def zernike_superposition(zern_surfaces, coeffs):
#     tic = time.time()
#     superposition = np.zeros(zern_surfaces[0].shape)
#     for i in range(len(zern_surfaces)):
#         superposition += zern_surfaces[i] * coeffs[i]
#     toc = time.time()
#     print("zernike_superposition ", toc - tic)
#     return superposition


def perform_fft(data):
    data = make_exponential(data)
    data = make_data_circle(data)
    data = expand_data_with_zeroz(data, 5)
    tic = time.time()
    data = np.fft.fft2(data)
    data = np.fft.fftshift(data, (0, 1))
    toc = time.time()
    print("fft itself ", toc - tic)
    data = make_data_abs(data)
    return data
