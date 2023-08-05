# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:26:49 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float32(io.imread('anelli.tif'))

plt.figure()
plt.title('Immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')

# calcolo la trasformata di Fourier

X = np.fft.fft2(x) # calcolo la tdf
Y = np.fft.fftshift(X) # shift nel range -0.5, 0.5
Z = np.log(1+np.abs(Y)) # applico operazione logaritmo

plt.figure()
plt.title('Spettro di ampiezza')
plt.imshow(np.abs(Z), clim = None, cmap = 'gray')

