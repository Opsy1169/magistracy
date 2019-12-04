import matplotlib.pyplot as plt

from ZernikeFunctions import *


def plot(values: np.ndarray):
    plt.axis('off')
    fig = plt.imshow(values, cmap=plt.cm.binary)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig('pict.png', bbox_inches='tight', pad_inches=0)
    plt.show()


def old_plot_method(x: np.ndarray, y: np.ndarray, values: np.ndarray):
    x, y = np.meshgrid(x, y)

    fig = plt.figure()
    ax = fig.gca(projection='3d', proj_type='ortho')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot_surface(x, y, np.array(values), cmap=plt.cm.binary, antialiased=False)

    plt.show()
