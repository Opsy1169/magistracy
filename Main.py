from Plotter import *
from DataUtil import *



if __name__ == "__main__":
    zernike_surface = get_zernike_data(zern_3_1, -2, 2, 151)
    zernike_surface = make_data_circle(zernike_surface)
    exponential_zernike = make_exponential(zernike_surface)
    exponential_zernike = np.fft.fft2(exponential_zernike)
    exponential_zernike = np.fft.fftshift(exponential_zernike, (0, 1))
    exponential_zernike = make_data_abs(exponential_zernike)

    x = np.linspace(-2, 2, 151)
    y = np.linspace(-2, 2, 151)
    checkPlot(x, y, zernike_surface)
    checkPlot(x, y, exponential_zernike)