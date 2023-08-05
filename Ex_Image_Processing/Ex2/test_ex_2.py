# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:10:50 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io


plt.close('all')

orig = np.float32(io.imread('spettro.jpg'))


h1, b1 = np.histogram(orig, np.arange(257))

x = np.log(orig+1)

h2, b2 = np.histogram(x, np.arange(257))

plt.figure()
plt.subplot(2,2,1)
plt.title('Immagine originale')
plt.imshow(orig, clim = None, cmap='gray')
plt.subplot(2,2,2)
plt.title('Immagine modificata')
plt.imshow(x, clim = None, cmap = 'gray')

# riga istogrammi
plt.subplot(2,2,3)
plt.title('Istogramma immagine originale')
plt.bar(np.arange(256), h1)
plt.subplot(2,2,4)
plt.title('Istogramma immagine modificata')
plt.bar(np.arange(256), h2)