# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:34:01 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

from skimage.transform import warp

plt.close('all')

x = np.float32(io.imread('lena.jpg'))

# ingrandiamo una sezione di 25x50 pixel intorno
# all'occhio di Lena

x = x[252:277, 240:290]
M = x.shape[0]; N = x.shape[1]



plt.figure()
plt.imshow(x, clim  = [0,255], cmap = 'gray')