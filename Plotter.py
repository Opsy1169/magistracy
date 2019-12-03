import cmath

import numpy as np
import matplotlib.pyplot as plt
from DataUtil import *
from  ZernikeFunctions import *
from mpl_toolkits.mplot3d import Axes3D


def checkPlot(x: np.ndarray, y: np.ndarray, values: np.ndarray):
    x, y = np.meshgrid(x, y)

    fig = plt.figure()
    ax = fig.gca(projection='3d', proj_type='ortho')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot_surface(x, y, np.array(values), cmap=plt.cm.binary, antialiased=False)

    plt.show()
