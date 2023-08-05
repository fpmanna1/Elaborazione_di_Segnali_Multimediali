# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:07:30 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
import skimage

from skimage.exposure import equalize_hist
from color_convertion import rgb2hsi, hsi2rgb
from skimage.color import rgb2yuv, yuv2rgb 
from skimage.feature import canny

plt.close('all')

# x = np.float32(io.imread('casa.tif'))/255
x = np.float32(io.imread('headCT.tif'))/255

# y = canny(x, sigma=3, low_threshold=0.0325, high_threshold=0.13)
y = canny(x, sigma=4, low_threshold=0.1, high_threshold=0.3)

plt.figure()
plt.subplot(1,2,1)
plt.title('Immagine originale')
plt.imshow(x, cmap = 'gray', clim = [0,1])
plt.subplot(1,2,2)
plt.title('Mappa dei contorni')
plt.imshow(y, cmap='gray', clim = [0,1])

# il bordo è sottile grazie alla non-maxima suppression