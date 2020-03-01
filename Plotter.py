import matplotlib.pyplot as plt

from ZernikeFunctions import *


# 69.5


def plot(values: np.ndarray):
    fig = plt.figure()
    fig.set_size_inches(2.56, 2.56)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    # plt.axis('off')
    fig = plt.imshow(values, cmap=plt.cm.binary)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig('pict.png', bbox_inches='tight', pad_inches=0, dpi=100)


def old_plot_method(x: np.ndarray, y: np.ndarray, values: np.ndarray):
    x, y = np.meshgrid(x, y)

    fig = plt.figure()
    ax = fig.gca(projection='3d', proj_type='ortho')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.plot_surface(x, y, np.array(values), cmap=plt.cm.binary, antialiased=False)

    plt.show()
