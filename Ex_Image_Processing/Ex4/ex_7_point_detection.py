# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:33:11 2023

@author: plett
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

x = np.float32(io.imread('turbina.jpg'))

# maschera per la rivelazione di un singolo punto
mask = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

y = ndi.correlate(x, mask, mode = 'reflect')

th =(90/100)*np.max(y) # soglia = 90% del valore massimo

z = y > th

plt.figure(figsize = (10,5))
plt.subplot(1,2,1)
plt.title('Immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')
plt.subplot(1,2,2)
plt.title('Singoli punti rilevati')
plt.imshow(z, clim = [0,1], cmap = 'gray')
