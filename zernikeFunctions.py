import cmath

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def zernM_one_N_minusone(r, phi):
    return 2*r*np.sin(phi)

def zernM_two_N_minustwo(r, phi):
    return np.sqrt(6)*r**2*np.sin(2*phi)


def checkPlot():
    x = np.linspace(-2, 2, 10)
    y = np.linspace(-2, 2, 10)
    z = []
    zfft = []
    justZernike = []

    for i in range(len(y)):
        arr = []
        arrWithoutExp = []
        for j in range(len(x)):
            r = np.sqrt(x[j]**2+y[i]**2)
            phi = np.arctan2(y[i], x[j])
            (r1, phi1) = cmath.polar(complex(x[j], y[i]))
            # print((r - r1), (phi == phi1))
            arr.append(np.exp(1j*zernM_one_N_minusone(r1, phi1)))
            # arrWithoutExp.append(zernM_one_N_minusone(r1, phi1))
            arrWithoutExp.append(zernM_two_N_minustwo(r1, phi1))
        zfft.append(arr)
        z.append(list(map(cmath.phase, arr)))
        justZernike.append(arrWithoutExp)

    x, y = np.meshgrid(x, y)

    print(zfft)
    # zfft = np.fft.fft2(zfft)
    # zfft = np.fft.fftshift(zfft, (0, 1))
    # zabs = []
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
    # fig = plt.figure()
    # ax = fig.gca(projection='3d', proj_type='ortho')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.plot_surface(x, y, np.array(zabs), cmap=plt.cm.binary, antialiased=False)
    #
    # plt.show()
    # print(x)
    # print(y)




checkPlot()
