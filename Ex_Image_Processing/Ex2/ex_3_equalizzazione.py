# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:33:18 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float32(io.imread('granelli.jpg')) 

plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')

n, b = np.histogram(x, np.arange(257)); # istogramma 
plt.figure(2); plt.bar(np.arange(256), n); # grafico a barre 
plt.axis([0,255,0,1.1*np.max(n)]); # estremi per ascisse e ordinate


from skimage.exposure import equalize_hist 
y = equalize_hist(x) # output e’ nel range [0,1] 
y = 255*y # lo convertiamo nel range [0, 255]

plt.figure(3); plt.imshow(y, clim=[0,255], cmap='gray');
plt.figure(4); plt.hist(y.flatten(), 256);
