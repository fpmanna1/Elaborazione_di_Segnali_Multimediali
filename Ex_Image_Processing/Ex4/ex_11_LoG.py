# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:24:44 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

from seg_utils import zero_crossing

plt.close('all')

x = np.float64(io.imread('angio.16bit.png'))

plt.figure(1)
plt.title('Immagine originale')
plt.imshow(x, clim = None, cmap = 'gray')

sigma = 5
y = ndi.gaussian_laplace(x, (sigma, sigma))

z = zero_crossing(y)


plt.figure(2)
plt.title('Mappa passaggi per lo zero')
plt.imshow(z, clim = [0,1], cmap = 'gray' )
