# -*- coding: utf-8 -*-
"""
Created on Tue May 16 12:40:26 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.reshape(np.fromfile('house.y', np.uint8), (512,512))
x = np.float64(x)

# definisco le maschere di Sobel : smoothing + derivata

m1 = [[-1, -2, -1], [0,0,0], [1,2,1]]
m2 = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

y1 = ndi.correlate(x, m1)
y2 = ndi.correlate(x, m2)

gradiente = np.abs(y1) + np.abs(y2); # gradiente

# per individuare una mappa binaria dei bordi faccio
# una sogliatura

msk = gradiente > 1.5*np.mean(gradiente)

plt.figure()
plt.subplot(1,3,1)
plt.title('immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')
plt.subplot(1,3,2)
plt.title('Gradiente')
plt.imshow(gradiente, clim = [0,255], cmap = 'gray')
plt.subplot(1,3,3)
plt.title('Mappa dei contorni')
plt.imshow(msk, clim = [0,1], cmap = 'gray')