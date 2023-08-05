# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:38:36 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

from color_convertion import rgb2hsi, hsi2rgb

plt.close('all')

x = np.float32(io.imread('fragole.jpg'))/255

x_hsi = rgb2hsi(x)

Ix = x_hsi[:,:,2]

Ix = ndi.gaussian_filter(Ix, 2)

x_hsi[:,:,2] = Ix

x = hsi2rgb(x_hsi)

plt.figure()
plt.imshow(x)




