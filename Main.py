from Plotter import *
from DataUtil import *

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

plt.show()

if __name__ == "__main__":
    zernike_surface = get_zernike_data(zern_9_3_1, -2, 2, 151)
    zernike_surface = make_data_circle(zernike_surface)

    aberration = perform_fft(zernike_surface)

    plot(zernike_surface)
    plot(aberration)
