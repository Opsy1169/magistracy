import cmath

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def zern_1_minus1(r, phi):
    return 2*r*np.sin(phi)

def zern_2_minus2(r, phi):
    return np.sqrt(6)*r**2*np.sin(2*phi)

def zern_3_1(r, phi):
    return 2*np.sqrt(2)*(3*r**3 - 2*r)*np.cos(phi)


def makeDataCircle(data):
    radius = np.floor(len(data)/2)
    mid_index = np.ceil(len(data)/2)
    for i in range(len(data)):
        for j in range(len(data[0])):
            x = abs(j-mid_index)
            y = abs(i-mid_index)
            elem_distance = np.floor(np.sqrt(x**2 + y**2))
            if elem_distance > radius:
                data[i][j] = 0
    return data


def fillData(function, left_border, right_border, points_count):
    x = np.linspace(left_border, right_border, points_count)
    y = np.linspace(left_border, right_border, points_count)
    # mean = rightBorder - (rightBorder+leftBorder)/2
    z = []
    zfft = []
    just_zernike = []
    # x = list(map(lambda val: val/mean, x))
    # y = list(map(lambda val: val / mean, y))

    for i in range(len(y)):
        arr = []
        arr_without_exp = []
        for j in range(len(x)):
            r = np.sqrt(x[j] ** 2 + y[i] ** 2)
            phi = np.arctan2(y[i], x[j])
            (r1, phi1) = cmath.polar(complex(x[j], y[i]))
            # print((r - r1), (phi == phi1))
            arr.append(np.exp(1j * function(r1, phi1)))
            # arrWithoutExp.append(zernM_one_N_minusone(r1, phi1))
            arr_without_exp.append(function(r1, phi1))
        zfft.append(arr)
        z.append(list(map(cmath.phase, arr)))
        just_zernike.append(arr_without_exp)
    return zfft, just_zernike

def checkPlot():
    zfft, justZernike = fillData(zern_3_1, -2, 2, 151)
    zfft = makeDataCircle(zfft)

    justZernike = makeDataCircle(justZernike)
    x = np.linspace(-1, 1, len(zfft))
    y = np.linspace(-1, 1, len(zfft))
    x, y = np.meshgrid(x, y)

    print(zfft)
    zfft = np.fft.fft2(zfft)
    zfft = np.fft.fftshift(zfft, (0, 1))
    zabs = list(map(lambda x: list(map(np.abs, x)), zfft))
    zabs = np.array(zabs)
    print(np.array(zabs))
    # for i in range(len(zfft)):
    #     temp = []
    #     for j in range(len(z[0])):
    #         temp.append(np.abs(zfft[i][j]))
    #     zabs.append(temp)
    #
    fig = plt.figure()
    ax = fig.gca(projection='3d', proj_type='ortho')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot_surface(x, y, np.array(justZernike), cmap=plt.cm.binary, antialiased=False)

    plt.show()
    fig = plt.figure()
    ax = fig.gca(projection='3d', proj_type='ortho')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot_surface(x, y, np.array(zabs), cmap=plt.cm.binary, antialiased=False)

    plt.show()
    # print(x)
    # print(y)




checkPlot()
