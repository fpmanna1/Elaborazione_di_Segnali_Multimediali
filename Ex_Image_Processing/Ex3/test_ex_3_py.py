# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:34:01 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage
import skimage.io as io

from skimage.exposure import equalize_hist

plt.close('all')

# provo ad eseguire l'operazione logaritmo e vedo come cambia
# sia l'immagine che l'istogramma

x = np.float32(io.imread('vista_aerea.jpg'))

h,b = np.histogram(x, np.arange(257))

plt.figure()
plt.subplot(1,2,1)
plt.imshow(x, clim = [0,255], cmap = 'gray')
plt.title('Immagine originale')
plt.subplot(1,2,2)
plt.bar(np.arange(256), h)

# y = 3*np.log(1+x)
y = x**4


h2, b2 = np.histogram(y, np.arange(1024))

plt.figure()
plt.subplot(1,2,1)
plt.imshow(y, clim = None, cmap = 'gray')
plt.title('Immagine dopo elaborazione')
plt.subplot(1,2,2)
plt.bar(np.arange(np.arange(1024)), h2)
