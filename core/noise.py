import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import scipy.ndimage


def base_grid(size_x=8):

    # X = np.linspace(-len_x/2, len_x/2, size_x)
    # Y = np.linspace(-len_x/2, len_x/2, size_x)

    sigma_y = 1.0
    sigma_x = 1.0

    # level_1 = np.random.rand(size_x, size_x)
    level_1 = np.random.rand(size_x, size_x) - 0.5

    # Apply gaussian filter
    sigma = [sigma_y, sigma_x]
    y = sp.ndimage.filters.gaussian_filter(level_1, sigma, mode='nearest')
    # plt.imshow(y)

    level_2 = np.random.rand(size_x * 2, size_x * 2) * 0.5 - 0.25

    level_3 = np.random.rand(size_x * 4, size_x * 4) * 0.25 - 0.125

    return level_1, level_2, level_3
