# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:33:38 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage

from skimage.transform import warp 

plt.close('all')

x = np.float64(io.imread('test.jpg')) 
plt.figure(1); plt.imshow(x,clim=[0,255],cmap='gray')

k = 3; h = np.ones((k,k))/(k**2) # definizione maschera per filtro media

y = ndi.correlate(x, h, mode='reflect') # applico la maschera con un'operazione
# a finestra scorrevole
# con mode specifico l'estensione ai bordi

# y = ndi.uniform_filter(x, size = 3, mode = 'reflect')

plt.figure(2); plt.imshow(y,clim=[0,255],cmap='gray');