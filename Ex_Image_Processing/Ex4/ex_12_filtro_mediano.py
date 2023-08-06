# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:41:34 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float32(io.imread('circuito_rumoroso.jpg'))

# applico il filtro mediano
y = ndi.generic_filter(x, np.median, (5,5))
# y = ndi.median filter(x, (5,5)) # alternativa

plt.figure()
plt.subplot(1,2,1); plt.imshow(x, clim = [0,255], cmap = 'gray')
plt.subplot(1,2,2); plt.imshow(y, clim = [0,255], cmap = 'gray')

