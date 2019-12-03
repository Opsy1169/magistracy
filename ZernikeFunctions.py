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

