# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:50:06 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')


from skimage.util import random_noise

x = np.float32(io.imread('lena.jpg'))

noisy = random_noise(x/255, mode='s&p') * 255
# la funzione random_noise richiede l'immagine nel range [0,1]

y = ndi.generic_filter(noisy, np.median, (5,5))

plt.figure()
plt.subplot(1,3,1)
plt.title('Immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')
plt.subplot(1,3,2)
plt.title('Immagine rumorosa')
plt.imshow(noisy, clim = [0,255], cmap = 'gray')
plt.subplot(1,3,3)
plt.title('Immagine filtrata')
plt.imshow(y, clim = [0,255], cmap='gray')
