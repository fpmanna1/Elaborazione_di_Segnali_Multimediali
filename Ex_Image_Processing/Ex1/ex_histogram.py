# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:16:45 2023

@author: plett
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

x = io.imread('dorian.jpg')

plt.figure()
plt.title('Immagine originale')
plt.imshow(x, cmap = 'gray', clim = [0,255])

h, b = np.histogram(x, np.arange(257)); # istogramma
plt.figure();
plt.bar(np.arange(256), h)              # grafico a barre
plt.axis([0,255,0,1.1*np.max(h)])       # estremi per ascisse e ordinate

# param. ritorno: istogramma e numero di intervalli (bins)



