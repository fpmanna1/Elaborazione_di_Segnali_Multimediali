# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:54:48 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage

from skimage.transform import warp 

plt.close('all')

x = np.float64(io.imread('rettangolo.jpg')) 
plt.figure(1); plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('immagine originale')

x = np.float64(io.imread('rettangolo.jpg')) 
plt.figure()



#Y = np.log(1+np.abs(np.fft.fftshift(X)))
plt.figure(2)
plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));