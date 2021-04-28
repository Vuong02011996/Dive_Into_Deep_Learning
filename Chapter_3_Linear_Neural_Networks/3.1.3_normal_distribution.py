import numpy as np
from d2l import mxnet as d2l
import matplotlib.pyplot as plt


def normal_distribution(x, mu, sigma):
    p = 1 / np.sqrt(2*np.pi*sigma**2)
    return p * np.exp(-0.5 * (x - mu)**2/sigma**2)


x = np.arange(-7, 7, 0.01)
params = [(0, 1), (0, 2), (3, 1)]
d2l.plot(x, [normal_distribution(x, mu, sigma) for mu, sigma in params], xlabel='z', ylabel='p(z)',
         figsize=(4.5, 2.5),
         legend=['mean {}, var {}'.format(mu, sigma) for mu, sigma in params])

plt.show()