# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:28:36 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x1 = np.float64(io.imread('volto.tif')) 
x2 = np.float64(io.imread('rettangolo.jpg')) 

# calcolo le trasformate di Fourier
X1 = np.fft.fft2(x1) # volto
X2 = np.fft.fft2(x2) # rettangolo

y = np.real(np.fft.ifft2(np.abs(X2) * np.exp(1j*np.angle(X1)))) 
plt.figure(1);
plt.imshow(y,clim=None,cmap='gray'); 
plt.title('Modulo rettangolo, Fase volto'); 
y = np.real(np.fft.ifft2(np.abs(X1) * np.exp(1j*np.angle(X2)))) 
plt.figure(2);
plt.imshow(y,clim=None,cmap='gray');
plt.title('Modulo volto, Fase rettangolo');