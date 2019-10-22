import cmath

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def zernM_one_N_minusone(r, phi):
    return 2*r*np.sin(phi)


def checkPlot():
    x = np.linspace(-2, 2, 50)
    y = np.linspace(-2, 2, 50)
    z = []
    zfft = []

    for i in range(len(y)):
        arr = []
        for j in range(len(x)):
            r = np.sqrt(x[j]**2+y[i]**2)
            phi = np.arctan2(y[i], x[j])
            arr.append(np.exp(1j*zernM_one_N_minusone(r, phi)))
        zfft.append(arr)
        z.append(list(map(cmath.phase, arr)))

    x, y = np.meshgrid(x, y)

    print(zfft)
    zfft = np.fft.fft2(zfft)
    zfft = np.fft.fftshift(zfft, (0, 1))
    zabs = []
    for i in range(len(zfft)):
        temp = []
        for j in range(len(z[0])):
            temp.append(np.abs(zfft[i][j]))
        zabs.append(temp)

    fig = plt.figure()
    ax = fig.gca( projection='3d', proj_type='ortho')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot_surface(x, y, np.array(z), cmap=plt.cm.binary, antialiased=False)

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
