from numpy.random import rand

from DataUtil import *
from Plotter import *

plt.show()

if __name__ == "__main__":
    tic = time.time()
    coeffs = rand(15)
    print(coeffs)
    zernike_surface = get_zernike_data(coeffs, -2, 2, 151)
    aberration = perform_fft(zernike_surface)
    plot(aberration)
    toc = time.time()
    print(toc - tic)
