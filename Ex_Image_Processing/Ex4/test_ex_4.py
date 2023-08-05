# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:59:16 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

plt.close('all')

x = np.float32(io.imread('angio.16bit.png'))

y = ndi.gaussian_laplace(x, (5, 5))

from seg_utils import zero_crossing

z = zero_crossing(y)

plt.figure()
plt.imshow(z, clim = [0,1], cmap = 'gray')






